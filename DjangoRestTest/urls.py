from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from MyAPI import urls as myapi_urls
from MyAPI.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('MyAPI/', include(myapi_urls)),
    path('MyAPI/', include('MyAPI.urls')),
    path('Todos/', include('todos.urls')),
    path('users/', include('users.urls')),
    path('v2/', include('versionedtodo.v2.urls')),
    path('v3/', include('versionedtodo.v3.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
