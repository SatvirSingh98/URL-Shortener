from django.contrib import admin
from django.urls import path
from URL.views import redirect_url, shortener

urlpatterns = [
    path('', shortener),
    path('<slug:slug>', redirect_url),
    path('admin/', admin.site.urls),
]
