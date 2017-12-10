from django.db import models


# Create your models here.
# model wzoru, takie kolumny ma w bazie
class PatternEntry(models.Model):
    name = models.CharField(max_length=255)  # nazwa
    visible = models.BooleanField(default=True)  # czy widoczny
    description = models.TextField(null=True, blank=True)  # opis opcjonalny
    image_file = models.ImageField(upload_to='images/')  # miniatura
    model_file = models.FileField(upload_to='pattern_zips/')  # plik modelu
    added_date = models.DateTimeField(auto_now=True)  # data dodania

    def __str__(self):  # metoda klasy, ktora zwraca krotka informacje tekstowa
        return "Rural pattern {0}, visible: {1}".format(self.name, self.visible)
