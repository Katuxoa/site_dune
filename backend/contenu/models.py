from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import FileExtensionValidator

class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.nom

class Texte(models.Model):
    CATEGORIES = [
        ('poeme', 'Poème'),
        ('blog', 'Blog'),
        ('roman', 'Roman'),
    ]
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    contenu = CKEditor5Field('Contenu', config_name='default', blank=True, null=True)
    couverture = models.ImageField(upload_to='couvertures/', blank=True, null=True)
    fichier_pdf = models.FileField(
        upload_to='pdfs/', 
        validators=[FileExtensionValidator(['pdf'])],
        blank=True, null=True, 
        verbose_name="Fichier PDF"
    )
    tags = models.ManyToManyField(Tag, blank=True)
    publie = models.BooleanField(default=False)
    vues = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre