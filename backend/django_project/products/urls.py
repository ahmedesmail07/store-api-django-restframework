from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("<int:pk>/delete/", views.ProductDelete.as_view(), name="product-delete"),
    path("<int:pk>/update/", views.ProductUpdate.as_view(), name="product-update"),
    # path("create/", views.ProductCreate.as_view()),
    path("create-list/", views.ProductListCreate.as_view(), name="product-list"),
    # path("list/", views.ProductList.as_view()),
    # path("", views.ProductMixinView.as_view()),
]
