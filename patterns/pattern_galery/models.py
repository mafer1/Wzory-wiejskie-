from django.db import models


# Create your models here.
# model wzoru, takie kolumny ma w bazie
class PatternEntry(models.Model):
    name = models.CharField(max_length=255)  # nazwa
    visible = models.BooleanField(default=True)  # czy widoczny
    description = models.TextField(null=True, blank=True)  # opis opcjonalny
    image_file = models.ImageField()  # miniatura
    model_file = models.FileField()  # plik modelu