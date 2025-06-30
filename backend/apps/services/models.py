from django.db import models
from core.models import BaseModel

class Service(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['name']
    