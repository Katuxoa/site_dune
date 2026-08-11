# Register your models here.
from django.contrib import admin
from .models import Texte, Tag

@admin.register(Texte)
class TexteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'publie', 'date_creation')
    list_filter = ('categorie', 'publie')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}

admin.site.register(Tag)