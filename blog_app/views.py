from django.shortcuts import render

from main_blog.models import Posts

def frontpage(request):
    posts = Posts.objects.all()
    return render(request, 'core/home.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')
