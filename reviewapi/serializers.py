from rest_framework import serializers
from .models import TV 

class TVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TV 
        fields = ('id', 'film', 'genre', 'network', 'year', 'rating')
        
        
        
        