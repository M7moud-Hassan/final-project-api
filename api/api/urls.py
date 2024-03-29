from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('profile/',include('profile_app.urls')),
    path('home/',include('home_app.urls')),
    path('chat/',include('chat_app.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
