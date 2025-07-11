from rest_framework import viewsets, permissions
from .models import Booking, Customer, Service
from .serializers import BookingReadSerializer, BookingWriteSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and creating bookings.
    """
    queryset = Booking.objects.all().select_related('customer__user').prefetch_related('services')
    permission_classes = [permissions.AllowAny] # Mude para IsAuthenticated em produção

    def get_serializer_class(self):
        # Usa o WriteSerializer para criar/atualizar e o ReadSerializer para ler
        if self.action in ['create', 'update', 'partial_update']:
            return BookingWriteSerializer
        return BookingReadSerializer
        