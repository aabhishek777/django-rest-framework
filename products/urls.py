
from django.urls import path
from . import views

from .views import product_alternate_view

urlpatterns = [
    path('create', product_alternate_view),
    path('list', product_alternate_view),
    path('<int:pk>/', product_alternate_view)
    # path('create', views.ProductCreateAPIView.as_view()),
    # path('list', views.ProductListCreateAPIView.as_view()),
    # path('<int:pk>/', views.ProductDetailsAPIView.as_view())
]
