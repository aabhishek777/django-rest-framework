
from django.urls import path
from . import views

from .views import product_alternate_view
from .views import product_mixin_api_view

urlpatterns = [
    # path('create', views.ProductCreateAPIView.as_view()),
    path('list', views.ProductListCreateAPIView.as_view()),
    # path('<int:pk>/', views.ProductDetailsAPIView.as_view())
    path('create', product_alternate_view),
    # path('list', product_alternate_view),
    path('<int:pk>/', product_alternate_view),
    # The line `path('', product_mixin_api_view)` in the urlpatterns list is defining a URL pattern
    # for an empty path. This means that when a user navigates to the base URL of the website (e.g.,
    # www.example.com/), the `product_mixin_api_view` function will be called to handle the request.
    path('', product_mixin_api_view)

]
