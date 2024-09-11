from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
import os
urlpatterns = [
    path('', views.chat_view, name='chat_page'),  # Renders the chat page HTML
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)