from django.shortcuts import render
from .models import PredictFamily, PredictSpecies

def predict_family_view(request):
    # เขียนโค้ดที่ต้องการ
    context = {}
    return render(request, 'predictor/predict_family.html', context)

def predict_species_view(request):
    # เขียนโค้ดที่ต้องการ
    context = {}
    return render(request, 'predictor/predict_species.html', context)
