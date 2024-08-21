from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the models
family_model = joblib.load('./family_model.pkl')
species_model = joblib.load('./species_model.pkl')

selected_columns = ['a(1-2)', 'b(2-3)', 'c(3-4)', 'd(4-5)', 'e(6-7)', 'f(7-10)', 'g(9-10)', 'h(9-15)', 'i(15-16)',
                    'j(14-15)', 'k(13-14)', 'l(13-17)', 'm(17-18)', 'n(1-18)', 'o(2-13)', 'p(3-12)', 'q(12-13)',
                    'r(5-12)', 's(11-14)', 't(8-11)', 'u(7-8)', 'v(8-9)', 'w(11-12)']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])

    # Predict Family
    family_prediction = family_model.predict(df[selected_columns])

    # Predict Species
    species_prediction = species_model.predict(df[selected_columns])

    return jsonify({
        'family_prediction': family_prediction[0],
        'species_prediction': species_prediction[0]
    })

if __name__ == '__main__':
    app.run(debug=True)
