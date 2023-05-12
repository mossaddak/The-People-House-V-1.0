from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=250, null=True, blank=True)
    author_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Author title")
    blog_title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Blog title")
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog")

    def __str__(self):
        return f"{self.pk}.{self.blog_title}"

