from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'product', viewset=views.ProductViewSet, base_name='products')
router.register(r'product_details', viewset=views.ProductDetailsViewSet, base_name='product_details')

urlpatterns = [
    url(r'product', views.ProductViewSet),
    url(r'product_details', views.ProductDetailsViewSet),

]
