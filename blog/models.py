from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)

    user=models.ForeignKey(User,on_delete=models.CASCADE , default=User)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    title=models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    user=models.ForeignKey(User,on_delete=models.CASCADE , default=User)
    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return reverse('view-comment',kwargs={'title':self.title})





