from rest_framework.viewsets import ModelViewSet
from ..models import Customer
from .seriallizers import CustomerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
