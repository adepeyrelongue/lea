from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.SourceSite)
admin.site.register(models.VisitedPage)
admin.site.register(models.Product)
