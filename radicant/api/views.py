from rest_framework import viewsets

from .serializers import EtfSerializer
from .models import Etf

class EtfViewSet(viewsets.ModelViewSet):
    queryset = Etf.objects.all()
    serializer_class = EtfSerializer
