from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Post(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='files/', null=True,blank=True)
    audio_file=models.FileField(upload_to='audio/', null=True,blank=True, help_text='upload audio recordings')
    
    class Meta:
        ordering=['-id']

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    username=models.CharField(max_length=50)
    comment=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    audio=models.FileField(upload_to='audio/', null=True,blank=True, help_text='upload audio recordings')

    def __str__(self):
        return self.username
    
class Reply(models.Model):
    repl=models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    name_of_user= models.CharField(max_length=50)
    reply=models.TextField()
    datef=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_of_user

    def get_absolute_url(self):
        return reverse("reply", kwargs={"pk": self.pk})
       

class Testimonies(models.Model):
    t_title=models.CharField(max_length=100)
    t_body=models.TextField()
    t_date=models.DateTimeField(auto_now_add=True)
    t_file=models.FileField(upload_to='files/', null=True,blank=True)
    t_audio_file=models.FileField(upload_to='audio/', null=True,blank=True, help_text='upload audio recordings')

    class Meta:
        ordering=['-id']

    

