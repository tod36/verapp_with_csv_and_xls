from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('proba/', proba),
    # path('exportexcel/', export_users_csv(), name='exportexcel'),
    # path('trucks/exportexcel/', views.exportexcel, name="exportexcel"),
    path('exportexcel/', exportexcel),
    # path('export_users_csv/', views.export_users_csv, name="export_users_csv"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
