from django.urls import path
from .views import index, details, getCoursesByCategory, getCoursesByCategoryId

# Hiçbir ek belirtilmediği taktirde: 127.0.0.1:8000/kurs olarak getir, yani varsayilan olarak bir sayfa belirttik.
# ama: 127.0.0.1:8000/kurslar/list dedigimiz zamanda yine yukaridaki sayfaya gitsin.

urlpatterns = [
    path('', index),   
    path('<kurs_id>', details, name="course_details"),
    path('kategori/<int:category_id>', getCoursesByCategoryId),
    path('kategori/<str:category_name>', getCoursesByCategory, name='courses_by_category'), # link alanina tanimlananlardan farkli bir deger girilirse burada bulunan dinamik alan calisir. Bu satir hep en asagida olmak zorunda.
]

