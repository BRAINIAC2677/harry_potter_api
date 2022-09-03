from rest_framework import serializers

from .models import Character

class CharacterReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Character
        fields = ['id', 'url', 'name', 'species', 'gender', 'house', 'patronus', 'wand_wood', 'wand_core']
        read_only_fields = ('__all__',)
    
    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])