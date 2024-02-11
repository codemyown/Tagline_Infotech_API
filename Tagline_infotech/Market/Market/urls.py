
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from api.views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls")),
    path("api/login",TokenObtainPairView.as_view()),
    path("api/refresh",TokenRefreshView.as_view()),
    path("api/register",RegisterView.as_view())
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
