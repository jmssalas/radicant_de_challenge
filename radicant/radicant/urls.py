from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('docs-schema/', get_schema_view(
        title="radicant Challenge"
    ), name='docs-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'docs-schema'}
    ), name='swagger-ui'),
]
