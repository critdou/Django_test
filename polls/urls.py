from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gaoyuan', views.gaoyuan, name='gaoyuan')
]