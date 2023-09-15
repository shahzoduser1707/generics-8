from rest_framework import serializers
from .models import MusicModel


class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = ('__all__')