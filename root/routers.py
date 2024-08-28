
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductListViewSet

routers = DefaultRouter()

routers.register('products-abc', ProductListViewSet)
