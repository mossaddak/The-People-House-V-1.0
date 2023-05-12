from django.contrib import admin
from .models import(
    NewsLetter,
    ElectionStart
)

# Register your models here.
admin.site.register(NewsLetter)
admin.site.register(ElectionStart)
