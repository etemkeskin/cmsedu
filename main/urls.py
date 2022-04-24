from django.urls import path
from main.views import *


app_name = 'main'

urlpatterns = [
    path('home/' , home, name='home'),
    path('about/' , about, name='about'),
]
