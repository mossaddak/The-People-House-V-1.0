from django.db import models
from .manager import CustomeUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"A user with that email already exists."})
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=20, null=True, blank=True)
    password_reset_token = models.CharField(max_length=20, null=True, blank=True)
    
    phone = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(null=True, blank=True, max_length=250)
    city = models.CharField(null=True, blank=True, max_length=250)
    country = models.CharField(null=True, blank=True, max_length=250)
    political_affiliation = models.CharField(null=True, blank=True, max_length=250)
    num_of_national_election_voted = models.CharField(blank=True, null=True, max_length=250, verbose_name="Number of national elections voted in")
    num_of_state_election_voted = models.CharField(blank=True, null=True, max_length=250, verbose_name="Number of state elections voted in")

    is_subscribed = models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'username']


    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.username}"
