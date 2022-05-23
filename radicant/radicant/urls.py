from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('swagger-ui-schema/', get_schema_view(
        title="radicant Challenge"
    ), name='swagger-ui-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'swagger-ui-schema'}
    ), name='swagger-ui'),
]
