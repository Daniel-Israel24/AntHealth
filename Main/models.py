from django.db import models
user_folder="static/"
# Create your models here.
class Image(models.Model):
    alt = models.TextField()
    marker = models.CharField(max_length=20)
    picture = models.ImageField(upload_to="%s/images" %user_folder)    

class Video(models.Model):
    alt = models.TextField()
    vid = models.FileField(upload_to='%svideos' %user_folder)
    marker = models.CharField(max_length=20)

class Chronology(models.Model):
    # owner = models.ForeignKey(Article, on_delete=models.CASCADE,  related_name='order')
    identifier = models.CharField(max_length=50)

class Message(models.Model):
    # owner = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='msg')
    txt = models.TextField()
    marker = models.CharField(max_length=20)

class SubArticle(models.Model):
    # master = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sub_article')
    starter = models.TextField()
    image = models.ManyToManyField(Image, related_name='image')

    video = models.ManyToManyField(Video, related_name='video')
    end = models.TextField()
    

class Article(models.Model):
    title=models.CharField(max_length=100)
    subarts = models.ManyToManyField(SubArticle, related_name='sub_art')
    
    # message = models.TextField()
    
