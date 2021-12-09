from django.http.response import HttpResponse
from django.shortcuts import render

from main_blog.models import Posts

def frontpage(request):
    posts = Posts.objects.filter(status=Posts.ACTIVE)
    return render(request, 'core/home.html', {'posts': posts})

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text, contest_type="text/plain"))
