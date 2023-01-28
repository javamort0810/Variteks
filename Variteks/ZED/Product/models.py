from django.db import models


# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    text = models.TextField()
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    text_uz = models.TextField()
    text_ru = models.TextField()


class Subcategory(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    text = models.TextField()
    name_uz = models.CharField(max_length=70)
    name_ru = models.CharField(max_length=70)
    text_uz = models.TextField()
    text_ru = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    title_uz = models.CharField(max_length=70,null=True)
    title_ru = models.CharField(max_length=70)
    text_uz = models.TextField()
    text_ru = models.TextField()


class Social_media(models.Model):
    item = models.FileField(upload_to="Social_media",null=True)
    url = models.URLField()
    is_active = models.BooleanField()


class Main_image(models.Model):
    file = models.FileField(upload_to="Main_image",null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Content_image(models.Model):
    file = models.FileField(upload_to="Content_image",null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

