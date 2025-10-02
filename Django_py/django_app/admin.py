from django.contrib import admin
from .models import ArticalModel
# Register your models here.
@admin.register(ArticalModel)
class AM(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title']
    search_fields = ['title','created_at']