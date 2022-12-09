from django.db import models
from datetime import datetime


class Pais(models.Model):
    nombre = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class User(models.Model):
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
