from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date


data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"Web gelistirme kategorisine ait kurslar",
    "mobil":"Mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title": "JavaScript Kursu",
            "description": "JavaScript Kurs açıklaması",
            "imageUrl": f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.orientsoftware.com%2FThemes%2FOrientSoftwareTheme%2FContent%2FImages%2Fblog%2F2021-12-16%2Fwhat-can-you-do-with-javascript-thumb.jpg&tbnid=0DJPYqCoG9YlLM&vet=12ahUKEwj5rPrjkOWDAxW67rsIHZ7-DoYQMygEegQIARBR..i&imgrefurl=https%3A%2F%2Fwww.orientsoftware.com%2Fblog%2Fwhat-can-you-do-with-javascript%2F&docid=10gVE9fJYTx1rM&w=720&h=460&q=javascript%20images&client=opera&ved=2ahUKEwj5rPrjkOWDAxW67rsIHZ7-DoYQMygEegQIARBR",
            "slug": "javascript-kursu",
            "date": date(2022, 10, 10),
            "is-active": True,
        },
        {
            "title": "Python Kursu",
            "description": "Python Kurs açıklaması",
            "imageUrl": f"https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D10223953689661794&tbnid=VrbT9cUet6n29M&vet=12ahUKEwjR6pT3kOWDAxUGhv0HHQ83A7wQMygKegQIARBC..i&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Fgroups%2Fpython%2F&docid=8N2I3Jh-s9VSqM&w=1640&h=924&q=python%20images&client=opera&ved=2ahUKEwjR6pT3kOWDAxUGhv0HHQ83A7wQMygKegQIARBC",
            "slug": "python-kursu",
            "date": date(2022, 9, 10),
            "is-active": True,
        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web Geliştirme açıklaması",
            "imageUrl": f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1200%2F0*M4bxiCIjcTK-2Xr6.jpeg&tbnid=y-fKDYcldejyJM&vet=12ahUKEwjWn-mDkeWDAxVAo_0HHQc6BrsQMygAegQIARBL..i&imgrefurl=https%3A%2F%2Fjavascript.plainenglish.io%2F10-best-web-development-software-for-web-developer-4d349f486d2a&docid=PXI6084aRPqMQM&w=1200&h=630&q=web%20development%20images&client=opera&ved=2ahUKEwjWn-mDkeWDAxVAo_0HHQc6BrsQMygAegQIARBL",
            "slug": "web-gelistirme-kursu",
            "date": date(2022, 8, 10),
            "is-active": True,
        },
    ],
    "categories": ["Programlama", "Web Geliştirme", "Mobil Uygulamalar"]
}


def index(request):
    category_list = list(data.keys())
    context = dict(
        categories = category_list,
    )
    return render(request, 'courses/index.html', context)

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} Kurs Detay Sayfasi")


# def getCoursesByCategory(request, category):
#     return HttpResponse(f"{ category } kategorisindeki kurs listesi")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        context = dict(
            category= category_name,
            category_text= category_text,
        )
        return render(request, 'courses/kurslar.html', context)
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)