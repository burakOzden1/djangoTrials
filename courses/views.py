from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date, datetime
from .models import Course
from .models import Category


data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"Web gelistirme kategorisine ait kurslar",
    "mobil":"Mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title": "JavaScript Kursu",
            "description": "JavaScript Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
            "imageUrl": f"1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False,
        },
        {
            "title": "Python Kursu",
            "description": "Python Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
            "imageUrl": f"2.jpg",
            "slug": "python-kursu",
            "date": date(2022, 9, 10),
            "isActive": True,
            "isUpdated": False,
        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web Geliştirme Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
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
    kurslar = Course.objects.filter(isActive=1)

    kategoriler = Category.objects.all()
    context = dict(
        categories = kategoriler,
        courses = kurslar,
    )
    return render(request, 'courses/index.html', context)


def details(request, slug):
    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()

    course = get_object_or_404(Course, slug= slug)

    context = dict(
        course = course
    )
    return render(request, "courses/details.html", context)

        

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