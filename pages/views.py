from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Anasayfa")

def hakkimizda(request):
    return HttpResponse("Hakkimizda")

def iletisim(request):
    return HttpResponse("Iletisim")
