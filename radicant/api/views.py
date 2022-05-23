from rest_framework import generics
from .serializers import EtfSerializer, FilterSerializer
from .models import Etf

class EtfListCreateAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Etf.objects.all()
        serializer = FilterSerializer(data=self.request.query_params)

        if serializer.is_valid():
            size_type = serializer.data['size_type']
            fund_category = serializer.data['fund_category']

        if size_type is not None and fund_category is not None:
            queryset = queryset.filter(size_type=size_type, fund_category=fund_category)
        elif size_type is not None:
            queryset = queryset.filter(size_type=size_type)
        elif fund_category is not None:
            queryset = queryset.filter(fund_category=fund_category)

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EtfSerializer
        if self.request.method == 'POST':
            return FilterSerializer
