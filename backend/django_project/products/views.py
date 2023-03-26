from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Detail View -> Single Product Detail -> PK
    # lookup_field = "pk"
    # lookup_field => Prodcut.objects.get(pk=#)
