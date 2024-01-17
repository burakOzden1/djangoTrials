from django.urls import path
from .views import kurslar, home


urlpatterns = [
    path('', home),
    path('anasayfa', home),
    path('kurslar', kurslar),
]

