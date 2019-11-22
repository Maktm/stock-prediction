from django.db import models
from django.contrib.auth import models as auth_models


class SavedStock(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
