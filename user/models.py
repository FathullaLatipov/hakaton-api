from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    address = models.CharField(max_length=130, null=True)
    resume = models.TextField(null=True)
    price = models.CharField(max_length=90, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
