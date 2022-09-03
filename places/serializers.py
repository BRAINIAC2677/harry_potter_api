from rest_framework import serializers

from .models import Place

class PlaceReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = ['id','url', 'name', 'category']
    
    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])