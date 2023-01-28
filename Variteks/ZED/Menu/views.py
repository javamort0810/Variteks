from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *


# Create your views here.

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = Aboutserializer


class About_itemViewSet(ModelViewSet):
    queryset = About_item.objects.all()
    serializer_class = Aboutitemserializer


class SertificatViewSet(ModelViewSet):
    queryset = Sertificat.objects.all()
    serializer_class = Sertificatserializer


# Translate About
class Aboutview(APIView):
    queryset = About.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = About.objects.all()
            serializer = About_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = About.objects.all()
            serializer = About_ru_serializer(queryset,many=True)
            return Response(serializer.data)


# Translate Aboutitem
class Aboutitemview(APIView):
    queryset = About_item.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = About_item.objects.all()
            serializer = About_item_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = About_item.objects.all()
            serializer = About_item_ru_serializer(queryset,many=True)
            return Response(serializer.data)