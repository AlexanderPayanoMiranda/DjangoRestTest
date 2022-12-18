from django.conf.urls.static import (static)
from django.contrib import (admin)
from django.urls import (
    path,
    include,
    re_path
)
from django.conf import (settings)

from rest_framework.permissions import (AllowAny)

from MyAPI.views import (index)

from drf_yasg import (openapi)
from drf_yasg.views import (get_schema_view)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Limited Todo API",
        default_version="v1",
        description="Simple Todo API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@contact.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[AllowAny],
    urlconf="TodoLimited.urls"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('MyAPI/', include(myapi_urls)),
    path('MyAPI/', include('MyAPI.urls')),
    path('Todos/', include('todos.urls')),
    path('TodoLimited/', include('TodoLimited.urls')),
    path('users/', include('users.urls')),
    path('g-views/', include('GViews.urls')),
    path('login-user/', include('LoginUser.urls')),
    path('v2/', include('versionedtodo.v2.urls')),
    path('v3/', include('versionedtodo.v3.urls')),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
