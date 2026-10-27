from django.contrib import admin
from django.urls import path, include

from restaurant.views import index

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Homepage
    path('', index, name='index'),

    # Restaurant API
    path('api/', include('restaurant.urls')),

    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]