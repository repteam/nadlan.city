from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('api/cards/', views.CardsVS.as_view({'get': 'list'})),
    path('api/image/', views.GalleryVS.as_view({'get': 'create', 'post': 'create'})),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Админ панель'
admin.site.site_title = 'Админ панель'
