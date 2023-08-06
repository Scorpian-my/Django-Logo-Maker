# image_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_form, name='image_form'),
    path('result', views.generate_image, name='generate_image'),
]
