from django.db import models


class Sympthon (models.Model):
    english_title = models.CharField(max_length=200)
    persian_title = models.CharField(max_length=200)
    

class Disease (models.Model):
    english_title = models.CharField(max_length=200)
    persian_title = models.CharField(max_length=200)
    sympthons = models.ManyToManyField(Sympthon)


