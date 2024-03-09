from django.contrib import admin
from .models import *

class CableTrayAdmin(admin.ModelAdmin):
    list_display = ('id', 'length_completed', 'size', 'area')

admin.site.register(cabletray, CableTrayAdmin)

# Register your models here.
