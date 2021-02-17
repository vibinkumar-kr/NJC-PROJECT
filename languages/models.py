from django.db import models

class language(models.Model):
    name = models.CharField(max_length=50)
    paradigam = models.CharField(max_length=50)

    def __str__(self):
        return self.name

