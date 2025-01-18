from django.contrib import admin
from app1.models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['user','text','image','date']
