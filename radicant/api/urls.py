from django.urls import path
from . import views

urlpatterns = [
    path('etfs/', views.EtfViewSet.as_view({'get': 'list'})),
]