from django.db import models
from django.db.models.fields import CharField, SlugField

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
