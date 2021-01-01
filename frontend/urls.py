from django.urls import path
from .views import index



app_name = 'frontend'


urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index),
    path('join/1', index)
]
