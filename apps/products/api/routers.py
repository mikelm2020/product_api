from rest_framework.routers import DefaultRouter

from apps.products.api.viewsets import ProductViewSet

router = DefaultRouter()
router.register(r"productos", ProductViewSet, basename="products")
urlpatterns = router.urls
