"""
URL configuration for LiveChadder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LiveChat.views import ChatAPI
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LiveChat.urls')),  # Include LiveChat app URLs
    path('api/chat/', ChatAPI.as_view(), name='chat_api'),  # New API endpoint
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)