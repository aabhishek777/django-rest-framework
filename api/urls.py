
from django.urls import path, include
from .views import app_home


urlpatterns = [
    path('', app_home),
    path('products/', include('products.urls')),
]
