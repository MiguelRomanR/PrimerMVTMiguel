from django.db import models
from django.forms import CharField

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age: models.IntegerField()
    relation = models.CharField(max_length=40)
    creation_date = models.DateField(auto_now_add=True)
