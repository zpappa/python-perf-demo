from django.db import models

# Create your models here.


class Company(models.Model):
    id = models.IntegerField(max_length=None, primary_key=True)
    name = models.TextField(max_length=255)
    symbol = models.TextField(max_length=10)
    address = models.TextField(max_length=255)
    state = models.TextField(max_length=2)
    zip = models.IntegerField()

    def __str(self):
        return self.name
