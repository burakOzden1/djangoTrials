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
            "imageUrl": f"https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "javascript-kursu",
            "date": date(2022, 10, 10),
            "is-active": True,
        },
        {
            "title": "Python Kursu",
            "description": "Python Kurs açıklaması",
            "imageUrl": f"https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "python-kursu",
            "date": date(2022, 9, 10),
            "is-active": False,
        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web Geliştirme açıklaması",
            "imageUrl": f"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2022, 8, 10),
            "is-active": True,
        },
    ],
    "categories": [
        {"id": 1, "name": "Programlama", "slug": "programlama"},
        {"id": 2, "name": "Web Geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name": "Mobil Uygulamalar", "slug": "mobil-uygulamalar"},
    ]
}


def index(request):
    kurslar = db["courses"]
    kategoriler = db["categories"]
    context = dict(
        categories = kategoriler,
        courses = kurslar,
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