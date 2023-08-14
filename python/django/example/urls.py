# example/urls.py
from django.urls import path

# from example.views import index


# urlpatterns = [
#     path('', index),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('generateAudio', views.generateAudio, name='generate_audio'),
]