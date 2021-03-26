from rest_framework import serializers

from .models import SomeCity


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeCity
        fields = ['id', 'city']
