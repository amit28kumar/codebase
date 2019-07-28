from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import products.urls as product_urls


router = DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/v1/', include(product_urls.router.urls)),
]
