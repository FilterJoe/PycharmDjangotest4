from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    ISBN13 = models.CharField(max_length=14,unique=True)
    def __unicode__(self):
        return self.title

# dumb test comment
# didn't work. So here is 2nd comment
# This comment is from my home computer, where I cloned the project. Does it make it to work computer?