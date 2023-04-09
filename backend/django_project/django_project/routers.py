from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
# "api/v2/route_path", ViewSet , basename = ''
urlpatterns = router.urls
