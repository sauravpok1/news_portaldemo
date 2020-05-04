from django.db import models

class Cat(models.Model):
    title=models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)
    rank=models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    menu_display = models.BooleanField(default=True)

    class Meta:
        abstract=True
