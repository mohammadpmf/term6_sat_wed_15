from django.db import models


class BlogPost(models.Model):
    STATUS = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    text = models.TextField() 
    status = models.CharField(max_length=1, choices=STATUS)