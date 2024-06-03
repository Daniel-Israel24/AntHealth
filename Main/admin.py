from django.contrib import admin
from . import models
# Register your models here.
# admin.site.site_header='Ant Health Website'
admin.site.site_title = 'Ant Health Website'
admin.site.site_header = 'FOR ALL YOUR MEDICAL ADVICE!'
admin.site.register(models.Article)
admin.register(models.Article)

admin.site.register(models.SubArticle)
admin.register(models.SubArticle)
admin.site.register(models.Image)

admin.site.register(models.Video)