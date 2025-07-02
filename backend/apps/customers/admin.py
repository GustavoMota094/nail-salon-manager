from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Customer

class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer Profile'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)
    
    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        return list(list_display) + ['get_phone_number']

    @admin.display(description='Phone Number')
    def get_phone_number(self, instance):
        return getattr(instance, 'customer_profile', None)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone_number', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone_number')

    @admin.display(description='Full Name')
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    