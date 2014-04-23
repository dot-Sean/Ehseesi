from django.db import models

# Create your models here.
class Search(models.Model):
    searchQuery = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
          return self.searchQuery
        
   # def modified_search_query(self):
    #      if self.searchQuery.find("livestream") == -1 and self.searchQuery.find("live stream") == -1:
   #         return self.searchQuery += " live stream"
   #       return self.searchQuery
#class Results(models.Model):
 #   query = models.ForeignKey(Search)
    #result =
    #link =