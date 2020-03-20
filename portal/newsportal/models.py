from django.db import models
from abstract.models import Cat

class CategoryManager(models.Manager):
    pass

class Category(Cat):
    objects=CategoryManager()
    view_count=models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table='category'

class News(models.Model):
    Nid=models.IntegerField(default=1)
    title=models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)
    rank=models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    CreatedDate = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=100)
    updatedDate = models.DateTimeField(auto_now=True)
    imageTitle= models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    mainNews = models.BooleanField(default=True)
    sliderKey = models.IntegerField(default=1)
    viewCount = models.IntegerField(default=0,null=True,blank=True)
    createdBy = models.CharField(max_length=100)
    updatedBy = models.CharField(max_length=100)

    def __str__(self):
        return self.title







