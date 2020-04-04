from django.db import models
from django import forms

# Create your models here.
class contactus(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=200
        )
    email = models.EmailField(
        verbose_name="Email address",
        unique=True
    )
    # subject = models.CharField(
    #     verbose_name="Subject",
    #     max_length=200
    # )
    message = models.TextField(
        verbose_name="Feedback please",
        null=True, blank=True
    )
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "contactus"