from django.db import models

# Create your models here.

class Choice(models.Model):
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()

