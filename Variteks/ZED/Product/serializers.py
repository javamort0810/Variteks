from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *


# Category
class Categoryserializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Category_uz
class Category_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    text = serializers.CharField(source='text_uz')

    class Meta:
        model = Category
        fields = ["name","text"]


# Category_ru
class Category_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')
    text = serializers.CharField(source='text_ru')

    class Meta:
        model = Category
        fields = ["name","text"]


# Subcategory
class Subcategoryserializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


# Subcategory_uz
class Subcategory_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    text = serializers.CharField(source='text_uz')

    class Meta:
        model = Subcategory
        fields = ["name","text"]


# Subcategory_ru
class Subcategory_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')
    text = serializers.CharField(source='text_ru')

    class Meta:
        model = Subcategory
        fields = ["name","text"]


# Product
class Productserializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Product_uz
class Product_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    text = serializers.CharField(source='text_uz')

    class Meta:
        model = Product
        fields = ["name","text"]


# Product_ru
class Product_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')
    text = serializers.CharField(source='text_ru')

    class Meta:
        model = Product
        fields = ["name","text"]


# Social
class Socialmidiaserializer(ModelSerializer):
    class Meta:
        model = Social_media
        fields = '__all__'

# Main
class Main_imageserializer(ModelSerializer):
    class Meta:
        model = Main_image
        fields = '__all__'

# Content
class Content_imageserializer(ModelSerializer):
    class Meta:
        model = Content_image
        fields = '__all__'
