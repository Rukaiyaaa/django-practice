from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice/', include('practice.urls')),
    path('', views.base_view , name='base_view')
]
