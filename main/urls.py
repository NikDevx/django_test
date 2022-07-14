from django.urls import re_path

from main.views import index_view

urlpatterns = [
    re_path(r'.*', index_view),
]
