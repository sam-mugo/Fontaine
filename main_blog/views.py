from django.shortcuts import get_object_or_404, render

from main_blog.models import Posts

# Create your views here.
def detail(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    
    return render(request, 'blog/detail.html', {'post': post})