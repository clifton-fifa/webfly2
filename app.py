from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

# Load your trained machine learning models
species_model = joblib.load('model/species_model.pkl')
family_model = joblib.load('model/family_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from the form
        form_data = {
            'a': float(request.form['a']),
            'b': float(request.form['b']),
            'c': float(request.form['c']),
            'd': float(request.form['d']),
            'e': float(request.form['e']),
            'f': float(request.form['f']),
            'g': float(request.form['g']),
            'h': float(request.form['h']),
            'i': float(request.form['i']),
            'j': float(request.form['j']),
            'k': float(request.form['k']),
            'l': float(request.form['l']),
            'm': float(request.form['m']),
            'n': float(request.form['n']),
            'o': float(request.form['o']),
            'p': float(request.form['p']),
            'q': float(request.form['q']),
            'r': float(request.form['r']),
            's': float(request.form['s']),
            't': float(request.form['t']),
            'u': float(request.form['u']),
            'v': float(request.form['v']),
            'w': float(request.form['w']),
        }

        features = [form_data[key] for key in sorted(form_data.keys())]

        # Predict using the loaded models
        species_prediction = species_model.predict([features])[0]
        species_accuracy = species_model.predict_proba([features])[0][species_model.classes_.tolist().index(species_prediction)] * 100

        family_prediction = family_model.predict([features])[0]
        family_accuracy = family_model.predict_proba([features])[0][family_model.classes_.tolist().index(family_prediction)] * 100

        # Determine the corresponding image path based on the family prediction
        family_image_path = {
            'Calliphoridae': 'static/assets/Calliphoridae.jpg',
            'Muscidae': 'static/assets/Muscidae.jpg',
            'Sarcophagidae': 'static/assets/Sarcophagidae.jpg'
        }.get(family_prediction, 'static/assets/picture1.png')

        return render_template('index.html',
                               speciesPrediction=species_prediction,
                               speciesAccuracy=species_accuracy,
                               familyPrediction=family_prediction,
                               familyAccuracy=family_accuracy,
                               familyImagePath=family_image_path)
    else:
        return render_template('index.html')

import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the request
        form_data = {
            'a': float(request.form['a']),
            'b': float(request.form['b']),
            'c': float(request.form['c']),
            'd': float(request.form['d']),
            'e': float(request.form['e']),
            'f': float(request.form['f']),
            'g': float(request.form['g']),
            'h': float(request.form['h']),
            'i': float(request.form['i']),
            'j': float(request.form['j']),
            'k': float(request.form['k']),
            'l': float(request.form['l']),
            'm': float(request.form['m']),
            'n': float(request.form['n']),
            'o': float(request.form['o']),
            'p': float(request.form['p']),
            'q': float(request.form['q']),
            'r': float(request.form['r']),
            's': float(request.form['s']),
            't': float(request.form['t']),
            'u': float(request.form['u']),
            'v': float(request.form['v']),
            'w': float(request.form['w']),
        }

        logging.debug(f"Form Data: {form_data}")

        features = [form_data[key] for key in sorted(form_data.keys())]

        # Predict using the loaded models
        species_prediction = species_model.predict([features])[0]
        species_accuracy = species_model.predict_proba([features])[0][species_model.classes_.tolist().index(species_prediction)] * 100

        family_prediction = family_model.predict([features])[0]
        family_accuracy = family_model.predict_proba([features])[0][family_model.classes_.tolist().index(family_prediction)] * 100

        logging.debug(f"Predictions: species={species_prediction}, family={family_prediction}")

        # Determine the corresponding image path based on the family prediction
        family_image_path = {
            'Calliphoridae': 'static/assets/Calliphoridae.jpg',
            'Muscidae': 'static/assets/Muscidae.jpg',
            'Sarcophagidae': 'static/assets/Sarcophagidae.jpg'
        }.get(family_prediction, 'static/assets/picture1.png')

        # Return the prediction results as a JSON response
        return jsonify({
            'species': species_prediction,
            'species_accuracy': species_accuracy,
            'family': family_prediction,
            'family_accuracy': family_accuracy,
            'image_path': family_image_path
        })
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
