from rest_framework import viewsets

from .models import ClientModel
from .serializer import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = ClientModel.objects.all()
