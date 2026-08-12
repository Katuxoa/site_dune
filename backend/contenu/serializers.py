from rest_framework import serializers
from .models import Texte

class TexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texte
        fields = '__all__' # send everything including pdf.url and image.url