from django.contrib import admin
from .models import Pin
# Register your models here.

# admin.site.register(Pin)

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']