from rest_framework import viewsets

from .serializers import EtfSerializer
from .models import Etf

class EtfViewSet(viewsets.ModelViewSet):
    serializer_class = EtfSerializer

    def get_queryset(self):
        queryset = Etf.objects.all()
        size_type = self.request.query_params.get('size_type')
        if size_type is not None:
            queryset = queryset.filter(size_type=size_type)
        return queryset
