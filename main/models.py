from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    email = models.CharField(null=True, blank=False, max_length=50)

    def __str__(self):
        return f"{self.pk}.{self.email}"
