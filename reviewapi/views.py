from django.shortcuts import render
from rest_framework import viewsets
from .models import TV 
from .serializers import TVSerializer



class TVView(viewsets.ModelViewSet):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
    
    
    
   

