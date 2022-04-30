from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path('<str:page_id>/', views.view_page, name='view_page'),
    path('<str:page_id>/edit/', views.edit_page, name='edit_page'),
    path('<str:page_id>/save/', views.save_page, name='save_page'),
]
