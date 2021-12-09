from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render



from .forms import CommentForm
from .models import Comment, Posts, Category

# Create your views here.
def detail(request, category_slug, slug, status=Posts.ACTIVE):
    post = get_object_or_404(Posts, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm() 
        
    return render(request, 'blog/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Posts.ACTIVE)
    
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')
    
    posts = Posts.objects.filter(status=Posts.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def about(request):
    return render(request, 'blog/about.html')