from django.db import models
from core.models import BaseModel
from apps.customers.models import Customer
from apps.services.models import Service

class Booking(BaseModel):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='bookings')
    services = models.ManyToManyField(Service, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Calculated price at the time of booking")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    admin_notes = models.TextField(blank=True, null=True, help_text="Internal notes for the admin")
    
    def __str__(self):
        return f"Booking for {self.customer.user.get_full_name()} at {self.start_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['start_time']
        