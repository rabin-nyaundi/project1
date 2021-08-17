from django.contrib import admin

# Register your models here.

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'address', 'details')
    
    
admin.site.register(Property, PropertyAdmin)
