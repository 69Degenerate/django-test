from django.contrib import admin
from .models import Contact,logs
# Register your models here.

admin.site.register(logs)
admin.site.register(Contact)