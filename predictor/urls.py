from django.urls import path
from . import views

urlpatterns = [
    path('predict_family/', views.predict_family_view, name='predict_family'),
    path('predict_species/', views.predict_species_view, name='predict_species'),
]
