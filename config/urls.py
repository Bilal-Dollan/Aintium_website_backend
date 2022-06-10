
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from aintium import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'config', views.index, 'index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name='index.html')),
    path("api/", include('aintium.urls')),
    path('swagger/', get_swagger_view(title='api')),
    path('auth/', obtain_auth_token),
    path('accounts/', include('allauth.urls')),
]
