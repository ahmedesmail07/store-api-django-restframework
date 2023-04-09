from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    """
    ModelViewSet >>>>
    This ViewSet can do the following HTTP VERPS :
    GET => pk or list view
    POST => For New Product
    UPDATE || PATCH => Update the content of the product
    DELETE => Delete The Current post

    """
