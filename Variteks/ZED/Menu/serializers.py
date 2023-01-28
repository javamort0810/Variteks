from ckeditor_uploader import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *


# About
class Aboutserializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


# About uz
class About_uz_serializer(serializers.HyperlinkedModelSerializer):
    text = serializers.CharField(source='text_uz')

    class Meta:
        model = About
        fields = ["text"]


# About ru
class About_ru_serializer(serializers.HyperlinkedModelSerializer):
    text = serializers.CharField(source='text_ru')

    class Meta:
        model = About
        fields = ["text"]


# About_item
class Aboutitemserializer(ModelSerializer):
    class Meta:
        model = About_item
        fields = '__all__'


# About_item_uz_
class About_item_uz_serializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title_uz')
    text = serializers.CharField(source='text_uz')

    class Meta:
        model = About_item
        fields = ["name", "title"]


# About_item_ru_
class About_item_ru_serializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title_ru')
    text = serializers.CharField(source='text_ru')

    class Meta:
        model = About_item
        fields = ["name", "title"]

# Sertificat
class Sertificatserializer(ModelSerializer):
    class Meta:
        model = Sertificat
        fields = '__all__'
