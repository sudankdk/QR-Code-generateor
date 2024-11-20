from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('generate/', views.generate_qr_code, name='generate_qr_code'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
