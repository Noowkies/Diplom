from django.contrib import admin
from .models import Tags

# Register your models here.

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass