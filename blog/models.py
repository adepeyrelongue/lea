from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.urls import reverse
import math


class Category(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class Product(models.Model):
      full_name =  models.CharField(max_length=500,default="")
      short_name =  models.CharField(max_length=500,default="")
      image_src = models.CharField(max_length=500,default="")
      resume = models.TextField(default="")
      pros = RichTextField(default="")
      cons = RichTextField(default="")
      rating = models.DecimalField(max_digits=3, decimal_places=1)
      url = models.CharField(max_length=1000,default="")
      speed_max = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      autonomy = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      user_weight_max = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      composition = models.CharField(max_length=500,default="")
      dimensions = models.CharField(max_length=500,default="")
      weight = models.DecimalField(max_digits=5, decimal_places=1,default=0)
      top_sales = models.BooleanField(default=False)
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True)
      price = models.DecimalField(max_digits=7, decimal_places=2,default=0)

      def __str__(self):
          return self.short_name
      
      def get_stars(self):
          full_stars = math.floor(self.rating)
          i = 1
          str = ""
          limit = full_stars

          while i <= limit:
            str+="<span class=\"fa fa-star checked\"></span>"
            i+=1
          
          if self.rating - full_stars > 0:
              str+="<span class=\"fa fa-star-half checked\"></span>"
              i += 1

          while i <= 5:
            str+="<span class=\"fa fa-star\"></span>"
            i+=1

          return str

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
