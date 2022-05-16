from django.urls import path, re_path

from .views import home_view

urlpatterns = [
    path(r'', home_view, name='home_view'),
]
