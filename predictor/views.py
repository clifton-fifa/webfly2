from django.shortcuts import render
from .forms import PredictionForm
from .models import predict_family, predict_species

def predict_family_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            family_prediction = predict_family(data)
            species_prediction = predict_species(data)
            return render(request, 'predictor/result.html', {
                'family_prediction': family_prediction,
                'species_prediction': species_prediction
            })
    else:
        form = PredictionForm()
    return render(request, 'predictor/form.html', {'form': form})
