from django.contrib import admin
from django.urls import path, include
from MyAPI import urls as myapi_urls
from MyAPI.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('MyAPI/', include(myapi_urls)),
    path('', include('todos.urls')),
]
