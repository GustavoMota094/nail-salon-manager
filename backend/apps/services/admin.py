from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
