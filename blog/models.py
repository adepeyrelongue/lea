from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.urls import reverse


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
      full_name =  models.CharField(max_length=500,default="")
      short_name =  models.CharField(max_length=500,default="")
      image_src = models.CharField(max_length=500,default="")
      resume = models.TextField(default="")
      pros = models.TextField(default="")
      cons = models.TextField(default="")
      rating = models.DecimalField(max_digits=3, decimal_places=1)
      url = models.CharField(max_length=1000,default="")
      speed_max = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      autonomy = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      user_weight_max = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      composition = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      dimensions = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      weight = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      top_sales = models.BooleanField(default=False)
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)

      def __str__(self):
          return self.full_name

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

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"slug" : self.slug})

class FirstPage(models.Model):
    title = models.CharField(max_length=200,default="")
    first_part = RichTextField(default="")
    last_part = RichTextField(default="")

    def __str__(self):
        return self.title
