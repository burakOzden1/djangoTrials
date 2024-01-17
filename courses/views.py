from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Anasayfa")

def kurslar(request):
    return HttpResponse("Kurs Listesi")

