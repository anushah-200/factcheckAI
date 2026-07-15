import os
import joblib
import pandas as pd
import numpy as np

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')

#Loading saved preprocessors and Random Forest model
print("Loading saved pipeline artifacts...")
rf_model = joblib.load(os.path.join(MODEL_DIR, 'random_forest.pkl'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
category_encoder = joblib.load(os.path.join(MODEL_DIR, 'category_encoder.pkl'))
model_encoder = joblib.load(os.path.join(MODEL_DIR, 'model_encoder.pkl'))
type_encoder = joblib.load(os.path.join(MODEL_DIR, 'type_encoder.pkl'))

#column order alignment matching training phase
FEATURE_ORDER = ['Category', 'Type', 'Model', 'ResponseLength', 'QuestionLength', 'ResponseCharacters', 'AverageWordLength']

def encode_value(val, encoder):
    """Safely encodes strings. Falls back to index 0 if value is unseen."""
    try:
        if val in encoder.classes_:
            return int(encoder.transform([val])[0])
        else:
            return 0
    except Exception:
        return 0

def predict_hallucination(feature_dict):

    encoded = feature_dict.copy()
    encoded['Category'] = encode_value(feature_dict['Category'], category_encoder)
    encoded['Type'] = encode_value(feature_dict['Type'], type_encoder)
    encoded['Model'] = encode_value(feature_dict['Model'], model_encoder)
    
    df = pd.DataFrame([encoded])[FEATURE_ORDER]
    
    scaled_features = scaler.transform(df)
    
    prediction = rf_model.predict(scaled_features)[0]
    probabilities = rf_model.predict_proba(scaled_features)[0]
    
    hallucination_prob = probabilities[1]
    
    return int(prediction), float(hallucination_prob)
