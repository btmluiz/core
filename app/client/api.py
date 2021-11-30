from rest_framework import viewsets
from rest_framework import permissions

from .models import ClientModel
from .serializer import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = ClientModel.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
