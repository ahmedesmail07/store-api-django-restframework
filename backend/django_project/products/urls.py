from django.urls import path
from . import views

urlpatterns = [
    # path("<int:pk>", views.ProductDetail.as_view()),
    # path("<int:pk>/delete/", views.ProductDelete.as_view()),
    # path("<int:pk>/update/", views.ProductUpdate.as_view()),
    # path("create/", views.ProductCreate.as_view()),
    path("create-list/", views.ProductListCreate.as_view()),
    # path("list/", views.ProductList.as_view()),
    path("", views.ProductMixinView.as_view()),
]
