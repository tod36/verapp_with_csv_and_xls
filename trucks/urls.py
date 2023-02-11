from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('proba/', proba),
    path('trucks/add_trucks/', add_trucks, name='add_trucks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
