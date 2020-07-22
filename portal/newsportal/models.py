from django.db import models
from abstract.models import Cat


class CategoryManager(models.Manager):
    pass


class Category(Cat):
    objects = CategoryManager()

    # view_count=models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    image_title = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0, null=True, blank=True)
    main_news = models.BooleanField(default=True)
    slider_key = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
