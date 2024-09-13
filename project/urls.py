from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Project API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   urlconf='project.urls',
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    path('api/', include('project.user.urls')),
    path('api/main/', include('project.main.urls')),
    path('api/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
)