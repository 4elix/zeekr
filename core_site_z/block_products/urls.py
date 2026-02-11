from django.urls import path
from rest_framework_nested import routers

from .swagger_settings import urlpatterns_swagger
from .views import ListProductPreview, ProductViewSet, TestDriveViewSet, TelegramAuthView


urlpatterns = [
    path('list_product/', ListProductPreview.as_view()),
    path('auth/telegram/', TelegramAuthView.as_view())
]

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

# products/{product_id:2}/test_drive/
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('test_drive', TestDriveViewSet, basename='product-test_drive')

urlpatterns += router.urls
urlpatterns += urlpatterns_swagger
urlpatterns += products_router.urls



