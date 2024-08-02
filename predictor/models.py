import joblib
import pandas as pd

# โหลดโมเดล
family_model = joblib.load('static/weight/family_model.pkl')
species_model = joblib.load('static/weight/species_model.pkl')

selected_columns = ['a(1-2)', 'b(2-3)', 'c(3-4)', 'd(4-5)', 'e(6-7)', 'f(7-10)', 'g(9-10)', 'h(9-15)', 'i(15-16)',
                    'j(14-15)', 'k(13-14)', 'l(13-17)', 'm(17-18)', 'n(1-18)', 'o(2-13)', 'p(3-12)', 'q(12-13)',
                    'r(5-12)', 's(11-14)', 't(8-11)', 'u(7-8)', 'v(8-9)', 'w(11-12)']

def predict_family(data):
    df = pd.DataFrame([data])
    prediction = family_model.predict(df[selected_columns])
    return prediction[0]

def predict_species(data):
    df = pd.DataFrame([data])
    prediction = species_model.predict(df[selected_columns])
    return prediction[0]
