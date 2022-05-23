from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EtfSerializer, FilterSerializer
from .models import Etf, Filter

class EtfListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['size_type', 'fund_category', ]

    def get_queryset(self):
        queryset = Etf.objects.all()
        query_params = self.request.query_params
        size_type, fund_category = None, None

        if query_params:
            serializer = FilterSerializer(data=query_params)
            if serializer.is_valid():
                size_type = serializer.data['size_type']
                fund_category = serializer.data['fund_category']
        else:
            latest_filter = Filter.objects.last()
            if latest_filter:
                serializer = FilterSerializer(latest_filter)
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
