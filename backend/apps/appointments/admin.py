from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_time', 'status', 'total_price')
    list_filter = ('status', 'start_time')
    search_fields = ('customer__user__first_name', 'customer__user__last_name', 'services__name')
    raw_id_fields = ('customer',)
