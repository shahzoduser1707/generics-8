from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MusicSerializers
from .models import MusicModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class GetMusic(generics.ListAPIView):
      queryset = MusicModel.objects.all()
      serializer_class = MusicSerializers
      permission_classes = (IsAuthenticated,)

class CreateMusic(generics.CreateAPIView):
      queryset = MusicModel.objects.all()
      serializer_class = MusicSerializers
    
class GetCreateMusic(generics.ListCreateAPIView):
      queryset = MusicModel.objects.all()
      serializer_class = MusicSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = MusicModel.objects.all()
      serializer_class = MusicSerializers