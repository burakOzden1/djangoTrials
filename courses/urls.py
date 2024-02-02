from django.urls import path
from .views import index, details, getCoursesByCategory, search, create_course, course_list, course_edit

# Hiçbir ek belirtilmediği taktirde: 127.0.0.1:8000/kurs olarak getir, yani varsayilan olarak bir sayfa belirttik.
# ama: 127.0.0.1:8000/kurslar/list dedigimiz zamanda yine yukaridaki sayfaya gitsin.

urlpatterns = [
    path('', index, name="index"),
    path('search', search, name="searh"),
    path('create-course', create_course, name="create_course"),
    path('course-list', course_list, name="course_list"),
    path('course-edit/<int:id>', course_edit, name="course_edit"),
    path('<slug:slug>', details, name="course_details"),
    # path('kategori/<int:category_id>', getCoursesByCategoryId),
    path('kategori/<slug:slug>', getCoursesByCategory, name='courses_by_category'), # link alanina tanimlananlardan farkli bir deger girilirse burada bulunan dinamik alan calisir. Bu satir hep en asagida olmak zorunda.
]

