from django.db import models


class Information_Face(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    time = models.DateTimeField()
