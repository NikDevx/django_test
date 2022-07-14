from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import urls as main_urls
from main.views import (index_view)

urlpatterns = [
    path('', index_view),
    path('', include(main_urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
