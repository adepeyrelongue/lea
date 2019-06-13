from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class SourceSite(models.Model):
      url = models.CharField(max_length=1000,default="")
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)

      def __str__(self):
         return self.url

class VisitedPage(models.Model):
      url = models.CharField(max_length=1000,default="")
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)
      source_site = models.ForeignKey(SourceSite, on_delete=models.SET_NULL, blank = True, null = True)

      def __str__(self):
          return self.url

class Product(models.Model):
      name =  models.CharField(max_length=500,default="")
      resume = models.TextField(default="")
      rating = models.DecimalField(max_digits=3, decimal_places=1)
      url = models.CharField(max_length=1000,default="")
      top_sales = models.BooleanField(default=False)
      top_three_sales = models.BooleanField(default=False)
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)

      def __str__(self):
          return self.url

class Post(models.Model):
    title = models.CharField(max_length=200,default="")
    slug = models.SlugField(unique=True, default="")
    image_src = models.CharField(max_length=500,default="")
    image_alt = models.CharField(max_length=500,default="")
    pitch = models.TextField(default="")
    body = RichTextField(default="")
    created = models.DateField(default=datetime.now)
    publish = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)
    visited_page = models.ForeignKey(VisitedPage, on_delete=models.SET_NULL, blank = True, null = True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.title
