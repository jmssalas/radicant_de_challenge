from django.urls import path
from . import views

urlpatterns = [
    path('etfs/', views.EtfListCreateAPIView.as_view()),
]