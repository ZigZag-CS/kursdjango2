from django.db import models

class Category(models.Model):
    """Primul model"""
    name = models.CharField("Nume", max_length=100)
    slug = models.SlugField("URL", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"

