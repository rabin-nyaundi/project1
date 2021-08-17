from django.urls import path

from . import views

urlpatterns = [
    path('', views.scrappe_view, name="index")
]
