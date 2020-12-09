from django.contrib import admin
from . import models


admin.site.register(models.AbstUser)
admin.site.register(models.Publication)