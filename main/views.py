from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('merhaba')


def about(request):
    return render(request, 'main/about.html')