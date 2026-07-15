import joblib


files = [
    "model/random_forest.pkl",
    "model/scaler.pkl",
    "model/category_encoder.pkl",
    "model/type_encoder.pkl",
    "model/model_encoder.pkl",
    "model/feature_names.pkl"
]


for file in files:

    print("\nTrying:", file)

    try:
        obj = joblib.load(file)
        print("SUCCESS:", type(obj))

    except Exception as e:
        print("FAILED")
        print(e)