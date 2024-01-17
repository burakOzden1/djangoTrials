from django.urls import path
from .views import index, about, contact


urlpatterns = [
    path('', index),  
    path('index', index),
    path('contact', contact),
    path('about', about),
]