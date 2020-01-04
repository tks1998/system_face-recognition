from django.db import models


class Information_Face(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    time = models.DateTimeField()


class IR2(models.Model):
    iddata = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    university = models.TextField(max_length=50)
