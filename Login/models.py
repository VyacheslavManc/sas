from django.db import models
from django.contrib.auth.models import User


class PersonalAccount(models):
    position = models.ForeignKey(User, verbose_name="Юзер", on_delete=models.CASCADE)
    