from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug
        
class Posts(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
     
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return '/%s/%s/' % (self.category.slug, self.slug)
        
        
class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    