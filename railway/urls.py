from django.urls import path

from . import views

urlpatterns = [
    path('', views.view, name='registration'),
    path('/upload', views.upload, name='upload')
]
