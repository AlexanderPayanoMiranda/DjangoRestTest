from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)


class TestValidation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    ip = models.GenericIPAddressField()
    integer = models.IntegerField()
    float = models.FloatField()
    decimal = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    time_now = models.TimeField()
