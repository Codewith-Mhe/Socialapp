from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='image/%y/%m/%d', )
    caption = models.TextField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    created_date= models.DateField(auto_now_add=True)
    like_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_liked', blank=True)
    

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering =('created', )

    def __str__(self):
        return self.body    
        