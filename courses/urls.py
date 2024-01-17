from django.urls import path
from .views import index, kurslar, details, getCoursesByCategory, getCoursesByCategoryId


urlpatterns = [
    path('', index),   # Hiçbir ek belirtilmediği taktirde: 127.0.0.1:8000/kurs olarak getir, yani varsayilan olarak bir sayfa belirttik.
    path('list', kurslar), # ama: 127.0.0.1:8000/kurslar/list dedigimiz zamanda yine yukaridaki sayfaya gitsin.
    path('<kurs_adi>', details),
    path('kategori/<int:category_id>', getCoursesByCategoryId),
    path('kategori/<str:category_name>', getCoursesByCategory, name='courses_by_category'), # link alanina tanimlananlardan farkli bir deger girilirse burada bulunan dinamik alan calisir. Bu satir hep en asagida olmak zorunda.
]

