from rest_framework import serializers

from .models import Spell

class SpellReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Spell
        fields = ['id', 'url','incantation', 'name', 'effect', 'light']
        read_only_fields = ('__all__',)

    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])