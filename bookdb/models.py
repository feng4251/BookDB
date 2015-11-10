# encoding: utf-8
from django.db import models

# Create your models here.

#class Publisher(models.Model):
#    name=models.CharField(max_length=30)
#    address=models.CharField(max_length=50)
#    city=models.CharField(max_length=60)
#    province=models.CharField(max_length=30)
#    country=models.CharField(max_length=50)
#    website=models.URLField()
#    
#    def __unicode__(self):
#            return self.name
#class Author(models.Model):
#    first_name=models.CharField(max_length=30)
#    last_name=models.CharField(max_length=40)
#    email=models.EmailField(max_length=50)
#    
#class Book(models.Model):
#    title=models.CharField(max_length=100)
#    authors=models.ManyToManyField(Author)
#    publisher=models.ForeignKey(Publisher)
#    publication_date=models.DateField()
#    

class Author(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=True)
    Country=models.CharField(max_length=100,null=True)

class Book(models.Model):
    ISBN=models.CharField(max_length=100,primary_key=True)
    Title=models.CharField(max_length=100,null=True)
    AuthorID=models.ForeignKey(Author)
    Publisher=models.CharField(max_length=100,null=True)
    PublishDate=models.DateField(null=True)
    Price=models.FloatField(null=True)


