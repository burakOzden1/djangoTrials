from django.urls import path
from .views import user_login, user_register, user_logout, change_password

# Hiçbir ek belirtilmediği taktirde: 127.0.0.1:8000/kurs olarak getir, yani varsayilan olarak bir sayfa belirttik.
# ama: 127.0.0.1:8000/kurslar/list dedigimiz zamanda yine yukaridaki sayfaya gitsin.

urlpatterns = [
    path('login', user_login, name="user_login"),
    path('register', user_register, name="user_register"),
    path('change-password', change_password, name="change_password"),
    path('logout', user_logout, name="user_logout"),
]