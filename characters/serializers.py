from rest_framework import serializers

from .models import Character

class CharacterReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'species', 'gender', 'house', 'patronus', 'wand_wood', 'wand_core']
        read_only_fields = ('__all__',)