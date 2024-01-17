from django.urls import path
from .views import home, hakkimizda, iletisim


urlpatterns = [
    path('', home),  
    path('anasayfa', home),
    path('anasayfa', iletisim),
    path('anasayfa', hakkimizda),
]