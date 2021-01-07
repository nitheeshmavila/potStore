from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    
    def all(self, request):
        products = Product.objects.all()
        serialzer = ProductSerializer(products, many=True)
        return Response(serialzer.data)

    def create(self, request):
        serialzer = ProductSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serialzer = ProductSerializer(product)
        return Response(serialzer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serialzer = ProductSerializer(instance=product, data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

