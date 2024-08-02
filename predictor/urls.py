from django.urls import path
from .views import predict_family_view

urlpatterns = [
    path('predict/', predict_family_view, name='predict_family'),
]
