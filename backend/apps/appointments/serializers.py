from rest_framework import serializers
from .models import Booking, Service
from apps.customers.serializers import CustomerSerializer
from apps.services.serializers import ServiceSerializer

class BookingReadSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

class BookingWriteSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = Booking
        fields = ('customer', 'services', 'start_time', 'admin_notes')

    def create(self, validated_data):
        services = validated_data.pop('services')
        
        total_price = sum(service.price for service in services)
        total_duration = sum(service.duration_minutes for service in services)
        
        # Calcula o end_time
        start_time = validated_data.get('start_time')
        end_time = start_time + timedelta(minutes=total_duration)
        
        validated_data['total_price'] = total_price
        validated_data['end_time'] = end_time
        
        booking = Booking.objects.create(**validated_data)
        booking.services.set(services)
        
        return booking
