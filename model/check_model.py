import joblib

try:
    # ลองโหลดโมเดล
    model = joblib.load('species_model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)
