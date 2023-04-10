from rest_framework import generics, mixins, permissions, authentication, authtoken
from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # Detail View -> Single Product Detail -> PK
    # lookup_field = "pk"
    # lookup_field => Prodcut.objects.get(pk=#)


class ProductDelete(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsStaffEditorPermission]  # Our Custom Permission


class ProductUpdate(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # permission_classes = [IsStaffEditorPermission]  # Our Custom Permission

    def perform_update(self, serializer):
        return super().perform_update(serializer)


# class ProductCreate(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsStaffEditorPermission]  # Our Custom Permission


class ProductListCreate(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    def perform_create(self, serializer):
        # email = serializer.validated_data.pop("email")
        # print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)

    # permission_classes = [permissions.IsAuthenticated]
    """
    Since using (StaffEditorPermissionMixin) there is no need for our permission classes
    """
    # permission_classes = [IsStaffEditorPermission]  # Our Custom Permission


# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsStaffEditorPermission]  # Our Custom Permission


class ProductMixinView(
    mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # this will be used incase of u pass a PK in the endpoint
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# This can be used as a GET METHOD
# GET ALL The products


# # Define Specific function to do all the above
# @api_view(["GET", "POST", "PUT", "DELETE"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#     if method == "GET":
#         if pk is not None:
#             # detail VIEW
#             queryset = Product.objects.filter(pk=pk)
#             if not queryset.exists():
#                 raise Http404
#             return Response()
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
#     if method == "POST":
#         # Create VIEW
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content")
#             if content is not None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#             print(serializer.data)
#         return Response(
#             {"Invalid": "Try Again"},
#         )
