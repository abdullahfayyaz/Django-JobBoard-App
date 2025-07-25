from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=True)