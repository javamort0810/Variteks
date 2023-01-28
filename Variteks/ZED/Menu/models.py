from ckeditor.fields import RichTextField
from django.db import models




# Create your models here.


class About(models.Model):
    text = RichTextField(null = True,blank=True,default=None)
    text_uz = RichTextField(null = True,blank=True,default=None)
    text_ru = RichTextField(null = True,blank=True,default=None)

class About_item(models.Model):
    title = models.CharField(max_length=50)
    picture = models.FileField(upload_to="About_item",null=True)
    text = models.TextField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    file = models.FileField(upload_to="Media/",null=True,blank=True)
    text_uz = models.TextField(null=True,blank=True)
    text_ru = models.TextField(null=True,blank=True)
    title_uz = models.CharField(max_length=50)
    title_ru = models.CharField(max_length=50)


class Sertificat(models.Model):
    file = models.FileField(upload_to="Sertificat",null=True)
    about_item = models.ForeignKey(About_item,on_delete=models.CASCADE)

