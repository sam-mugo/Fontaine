from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        
        
class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    