
from django.urls import path, urls

from . import views

urlpatterns = [
    path('', views.index, name='index')
]

