from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from hack.views import get_api, get_new_api

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('get-api/', get_api, name='get_api'),
    path('get-new-api/', get_new_api, name='get_new_api'),
]
