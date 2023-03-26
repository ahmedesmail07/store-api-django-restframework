from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Detail View -> Single Product Detail -> PK
    # lookup_field = "pk"
    # lookup_field => Prodcut.objects.get(pk=#)


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Define Specific function to do all the above
@api_view(["GET", "POST", "PUT", "DELETE"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # detail VIEW
            queryset = Product.objects.filter(pk=pk)
            if not queryset.exists():
                raise Http404
            return Response()
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
    if method == "POST":
        # Create VIEW
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")
            if content is not None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
            print(serializer.data)
        return Response(
            {"Invalid": "Try Again"},
        )
