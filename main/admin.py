from django.contrib import admin
from .models import(
    NewsLetter,
    ElectionStart,
    Invitation
)

# Register your models here.
admin.site.register(NewsLetter)
admin.site.register(ElectionStart)
admin.site.register(Invitation)
