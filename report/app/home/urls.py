from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index),
    path('upload/',views.upload,name ='upload'),
    path('screens/', views.screens, name="screens"),
    path('indexfr/', views.getframe)
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.IMG_URL,document_root = settings.IMG_ROOT)