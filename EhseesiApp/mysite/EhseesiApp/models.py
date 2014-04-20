from django.db import models

# Create your models here.
class Search(models.Model):
    searchQuery = models.CharField(max_length=100)

#class Results(models.Model):
    #query = models.ForeignKey(Search)
    #result =
    #link =