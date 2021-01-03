
from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'all',
        'post': 'create'
    })),
    # path('products/<str:pk>', ProductViewSet.as_view({
    #     'get': 'retrive',
    #     'put': 'update',
    #     'delete': 'remove'
    # }))
]

