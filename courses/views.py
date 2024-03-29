from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Course, UploadModel
from .models import Category, Slider
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from django.contrib.auth.decorators import login_required, user_passes_test

# data = {
#     "programlama":"programlama kategorisine ait kurslar",
#     "web-gelistirme":"Web gelistirme kategorisine ait kurslar",
#     "mobil":"Mobil kategorisine ait kurslar",
# }

# db = {
#     "courses": [
#         {
#             "title": "JavaScript Kursu",
#             "description": "JavaScript Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
#             "imageUrl": f"1.jpg",
#             "slug": "javascript-kursu",
#             "date": datetime.now(),
#             "isActive": True,
#             "isUpdated": False,
#         },
#         {
#             "title": "Python Kursu",
#             "description": "Python Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
#             "imageUrl": f"2.jpg",
#             "slug": "python-kursu",
#             "date": date(2022, 9, 10),
#             "isActive": True,
#             "isUpdated": False,
#         },
#         {
#             "title": "Web Geliştirme Kursu",
#             "description": "Web Geliştirme Kurs açıklaması, Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla nihil nam corrupti dolores exercitationem alias omnis recusandae quam id asperiores.",
#             "imageUrl": f"3.jpg",
#             "slug": "web-gelistirme-kursu",
#             "date": date(2022, 8, 10),
#             "isActive": True,
#             "isUpdated": True,
#         },
#     ],
#     "categories": [
#         {"id": 1, "name": "Programlama", "slug": "programlama"},
#         {"id": 2, "name": "Web Geliştirme", "slug": "web-gelistirme"},
#         {"id": 3, "name": "Mobil Uygulamalar", "slug": "mobil-uygulamalar"},
#     ]
# }


def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()
    sliders = Slider.objects.filter(is_active=True)

    context = dict(
        categories = kategoriler,
        courses = kurslar,
        sliders = sliders,
    )
    return render(request, 'courses/index.html', context)

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    # if not request.user.is_superuser:
    #     return redirect("index")
    # Bu ifade yerine yukarida decorator kullandik
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/kurs")
    else:
        form = CourseCreateForm()
    context = dict(
        form = form,
    )
    return render(request, "courses/create-course.html", context)

# @login_required() # settings.py dosyasinde bu ifadenin gidecegi konumu belirttik, varsayilan olarak kendisi oradan alıyor, bizim yazmamıza gerek yok. Bu ifade ile kullaninin uygulamamiza giris yapmasi yeterli ama biz asagidaki fonksiyona sadece superuser olan kullanicilari erisebilmesini istiyoruz. Bunu da:
@user_passes_test(isAdmin) # ifadesi yapar.
def course_list(request):
    # if not request.user.is_superuser:
    #     return redirect("index")
    # Bu ifade yerine yukarida decorator kullandik
    kurslar = Course.objects.all()
    context = dict(
        courses = kurslar,
    )
    return render(request, 'courses/course-list.html', context)

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    context = dict(
        form = form,
    )
    return render(request, "courses/edit-course.html", context)

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        # Course.objects.get(pk=id).delete() # (Course.objects.get(pk=id)) ifadesi course ifadesine esit oldugu icin asagidaki gibi duzenledik.
        course.delete()
        return redirect("course_list")

    context = dict(
        course = course,
    )
    return render(request, "courses/course-delete.html", context)

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return render(request ,"courses/success.html")
    else:
        form = UploadForm()
    
    context = dict(
        form = form,
    )
    return render(request, "courses/upload.html", context)


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    context = dict(
        categories = kategoriler,
        courses = kurslar,
    )
    return render(request, 'courses/search.html', context)


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

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date") # tarihe gore siralamasini soyledik.
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2) # her sayfada 2 adet kurs olsun
    page = request.GET.get("page", 1) # varsayilan olarak ilk sayfayi al
    page_obj = paginator.page(page) # page sayfasindaki urun bilgilerini getir. # get_page yerine page de kullanabilirsin.
    # print(page_obj.paginator.count) # kurs sayisini verir.
    # print(page_obj.paginator.num_pages) # sayfa sayisini verir.


    context = dict(
        categories = kategoriler,
        page_obj = page_obj,
        seciliKategori = slug,
    )
    return render(request, 'courses/list.html', context)


# def getCoursesByCategoryId(request, category_id):
#     category_list = list(data.keys())
#     if (category_id > len(category_list)):
#         return HttpResponseNotFound("Yanlış Kategori Seçimi")
#     category_name = category_list[category_id - 1]

#     redirect_url = reverse('courses_by_category', args=[category_name])

#     return redirect(redirect_url)