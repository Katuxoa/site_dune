# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Texte

def home(request):
    poemes = Texte.objects.filter(categorie='poeme', publie=True)
    return render(request, 'home.html', {'poemes': poemes})

def detail_texte(request, slug):
    texte = get_object_or_404(Texte, slug=slug, publie=True)
    texte.vues += 1
    texte.save()
    return render(request, 'detail.html', {'texte': texte})