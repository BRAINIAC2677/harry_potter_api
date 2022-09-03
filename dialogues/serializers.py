from rest_framework import serializers

from chapters.models import Chapter
from places.models import Place
from characters.models import Character
from .models import Dialogue

class DialogueReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    chapter = serializers.PrimaryKeyRelatedField(queryset=Chapter.objects.all())
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())

    class Meta:
        model = Dialogue
        fields = ['id', 'url','chapter', 'place', 'character', 'dialogue']
        read_only_fields = ('__all__',)
    
    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])