from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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
# UPDATE BLOG
def update_blog(request, id):
    context = {}
    post = Post.objects.filter(id = id).first()

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()

    context['post'] = post
    return render(request, 'blog/update.html', context) 

#DELETE BLOG
def delete_blog(request, id):
    Post.objects.filter(id = id).delete()
    return HttpResponseRedirect(reverse('main:blog_list'))

def blog_list(request):

    context = {}
    posts = Post.objects.all()
    context['posts'] = posts

   

    return render(request, 'blog/blog_list.html', context)