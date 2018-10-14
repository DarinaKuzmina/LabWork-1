from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2048)
    publish_date = models.DateTimeField('date published')
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title