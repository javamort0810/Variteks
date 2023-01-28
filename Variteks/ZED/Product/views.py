from django.shortcuts import render

from Product.models import *
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from Product.serializers import *

from Product.models import *




# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = Subcategoryserializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer


class Social_mediaViewSet(ModelViewSet):
    queryset = Social_media.objects.all()
    serializer_class = Subcategoryserializer


class Main_imageViewSet(ModelViewSet):
    queryset = Main_image.objects.all()
    serializer_class = Main_imageserializer


class Content_imageViewSet(ModelViewSet):
    queryset = Content_image.objects.all()
    serializer_class = Content_imageserializer

# Translate Category
class Categoryview(APIView):
    queryset = Category.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Category.objects.all()
            serializer = Category_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Category.objects.all()
            serializer = Category_ru_serializer(queryset,many=True)
            return Response(serializer.data)


# Translate Subcategory
class Subcategoryview(APIView):
    queryset = Subcategory.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Subcategory.objects.all()
            serializer = Subcategory_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Subcategory.objects.all()
            serializer = Subcategory_ru_serializer(queryset,many=True)
            return Response(serializer.data)


# Translate Subcategory
class Productview(APIView):
    queryset = Product.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Product.objects.all()
            serializer = Product_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Product.objects.all()
            serializer = Product_ru_serializer(queryset,many=True)
            return Response(serializer.data)







