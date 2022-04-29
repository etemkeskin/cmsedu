from django.http import HttpResponse
from django.shortcuts import render
from main.models import Post


def home(request):
    return HttpResponse('merhaba')


def about(request):
    return render(request, 'main/about.html')


# Functional Based views

# CREATE POST
def blog_create(request):

    if request.method == "POST":
        print(request)
        Post.objects.create(user_id = 1, title = request.POST["title"], content = request.POST["content"])

    return render(request, 'blog/create.html')


def blog_list(request):

    context = {}
    posts = Post.objects.all()
    context['posts'] = posts

   

    return render(request, 'blog/blog_list.html', context)