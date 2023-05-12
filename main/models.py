from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    email = models.CharField(null=True, blank=False, max_length=50)

    def __str__(self):
        return f"{self.pk}.{self.email}"
    

class ElectionStart(models.Model):
    date = models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return f"{self.pk}.{self.date}"
    

class Invitation(models.Model):
    name = models.CharField(max_length=250, null=True, blank=False)
    email = models.CharField(max_length=250, null=True, blank=False)
    state = models.CharField(max_length=250, null=True, blank=False)
    phone = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return f"{self.pk}.{self.name}"
