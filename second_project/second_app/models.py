from django.db import models

# Create your models here.

class User(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    email = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.first} {self.last}'