 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from Menu.views import *
from Product.views import *

from ZED_IT import settings

router = DefaultRouter()
router.register('Product', ProductViewSet, basename='product')
router.register("About", AboutViewSet, basename="About")
router.register("About_item", About_itemViewSet, basename="About_item")
router.register('Sertificat', SertificatViewSet, basename="Sertificat")
router.register("Category", CategoryViewSet, basename="Category")
router.register("Subcategory", SubcategoryViewSet, basename="Subcategory")
router.register("Social_media", Social_mediaViewSet, basename="Social_media")
router.register("Main_image", Main_imageViewSet, basename="Main_image")
router.register("Content_image", Content_imageViewSet, basename="Content_image")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("", include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

