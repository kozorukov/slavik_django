from django.db import models


class Twitters(models.Model):
    text = models.TextField('Twitters')
