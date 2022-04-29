from django.urls import path
from main.views import *


app_name = 'main'

urlpatterns = [
    path('home/' , home, name='home'),
    path('about/' , about, name='about'),

    path('blogs/' , blog_list, name='blog_list'),

    path('blogs/create/' , blog_create, name='blog_create')
    # path('blogs/<int:id>/' , get_blog, name='get_blog')
    # path('blogs/<int:id>/update/' , update_blog, name='update_blog')
    # path('blogs/<int:id>/delete/' , delete_blog, name='delete_blog')
]
