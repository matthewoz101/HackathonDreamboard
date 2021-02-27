from django.db import models


# Create your models here.

class dream(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dreamItem = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.dreamItem
