from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('api/')),
    path('admin/', admin.site.urls),
    path('api/authentication/', include('authentication.urls')),
]
