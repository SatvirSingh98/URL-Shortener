from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from URL.views import redirect_url, shortener

urlpatterns = [
    path('', shortener),
    path('<slug:slug>', redirect_url),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
