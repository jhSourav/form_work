from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Division(models.Model):
    name=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    population=models.IntegerField(max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    population = models.IntegerField(max_length=30)
    div = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name