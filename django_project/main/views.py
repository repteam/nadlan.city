from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializer import CardsSerializer
from .models import Cards, Gallery
from rest_framework.response import Response
from django.http import FileResponse
from urllib.parse import unquote
# Create your views here.


class CardsVS(ViewSet):
    def list(self, request):
        serializer = CardsSerializer(instance=Cards.objects.all(), many=True)
        return Response (serializer.data)
    
class GalleryVS(ViewSet):
    def create(self, request):
        if request.POST.get('id') != None and Gallery.objects.filter(id=request.data['id']).exists():
            obj = Gallery.objects.get(id=request.data['id'])
            url = list({obj.image.url})[0][7:]
            f = open(f'/home/django/django_project/image/{unquote(url)}', 'rb')
            return FileResponse(f)
        else:
            return Response({'detail': 'error'})
