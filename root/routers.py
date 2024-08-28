
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductListViewSet

routers = DefaultRouter()

routers.register(r'products-abc', ProductListViewSet, basename='products')

urlpatterns = routers.urls
