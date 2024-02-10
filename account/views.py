from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

from account.forms import LoginUserForm, NewUserform, UserPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error": "Yetkiniz yok."})
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

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
                return render(request, "account/login.html", {"form":form})
        else:
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def user_register(request):
    if request.method == "POST":
        form = NewUserform(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect("index")
        else:
            context = dict(
                form = form,
            )
            return render(request, "account/register.html", context)

    else:
        form = NewUserform()
        context = dict(
            form = form,
        )
        return render(request, "account/register.html", context)

def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parola Güncellendi.")
            return redirect("change_password")
        else:
            context = dict(
                form = form,
            )
            return render(request, "account/change-password.html", context)
        
    form = UserPasswordChangeForm(request.user)
    context = dict(
        form = form,
    )
    return render(request, "account/change-password.html", context)


    context = dict(
        form = form,
    )
    return render(request, "account/change-password.html", context)

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")