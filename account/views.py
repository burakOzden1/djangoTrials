from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error": "Yetkiniz yok."})
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect("index")
            messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
            nextUrl = request.GET.get("next", None)
            if nextUrl is None:
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            messages.add_message(request, messages.ERROR, "Kullanıcı adı ya da parola yanlış")
            return render(request, "account/login.html")
    else:             
            return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                context = dict(
                    error = "Bu isimde bir kullanıcı mevcut. Lütfen farklı bir kullanıcı ismi belirleyin.",
                    username = username,
                    email = email,
                )
                return render(request, "account/register.html", context)
            else:
                if User.objects.filter(email=email).exists():
                    context = dict(
                        error = "Bu eposta adresi kullanılıyor.",
                        username = username,
                        email = email,
                    )
                    return render(request, "account/register.html", context)
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("user_login")

        else:
            context = dict(
                error = "parolalar eşleşmiyor.",
            )
            return render(request, "account/register.html", context)
    else:
        return render(request, "account/register.html")

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")