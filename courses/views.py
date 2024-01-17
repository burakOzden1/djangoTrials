from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date, datetime


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
            "imageUrl": f"1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False,
        },
        {
            "title": "Python Kursu",
            "description": "Python Kurs açıklaması",
            "imageUrl": f"2.jpg",
            "slug": "python-kursu",
            "date": date(2022, 9, 10),
            "isActive": False,
            "isUpdated": False,
        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web Geliştirme açıklaması",
            "imageUrl": f"3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2022, 8, 10),
            "isActive": True,
            "isUpdated": True,
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