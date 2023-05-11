from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250, null=True, blank=False)
    email = models.CharField(max_length=250, null=True, blank=False)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField(null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.name}"



