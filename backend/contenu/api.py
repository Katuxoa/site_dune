from rest_framework import serializers, viewsets
from .models import Texte

class TexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texte
        fields = ['id', 'titre', 'slug', 'categorie', 'contenu', 'couverture', 'fichier_pdf', 'vues', 'date_creation']

class TexteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Texte.objects.filter(publie=True)
    serializer_class = TexteSerializer
    lookup_field = 'slug'