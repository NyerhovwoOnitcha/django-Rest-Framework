from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    cellphone_number = models.CharField(max_length=15, blank=True, null=True)

class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, default="NonAssigned")

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


