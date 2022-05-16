from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),    
    path('', include('apps.home.urls')),
    path('chat/', include('apps.chat.urls')),
    path('wiki/', include('apps.wiki.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
