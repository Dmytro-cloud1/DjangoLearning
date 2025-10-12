from django.contrib import admin
from .models import ArticalModel, Aliens
# Register your models here.
@admin.register(ArticalModel)
class AM(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title']
    search_fields = ['title','created_at']

@admin.register(Aliens)
class Alien_admin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['name']
    search_fields = ['name','age']