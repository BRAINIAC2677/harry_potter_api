from rest_framework import serializers

from .models import Movie

class MovieReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id', 'url', 'title', 'release_year', 'runtime', 'budget', 'box_office_revenue']
        read_only_fields = ('__all__',)

    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])