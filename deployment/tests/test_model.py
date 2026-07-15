import joblib
import pandas as pd


print("Loading model...")

model = joblib.load(
    "model/random_forest.pkl"
)

scaler = joblib.load(
    "model/scaler.pkl"
)

category_encoder = joblib.load(
    "model/category_encoder.pkl"
)

type_encoder = joblib.load(
    "model/type_encoder.pkl"
)

model_encoder = joblib.load(
    "model/model_encoder.pkl"
)

feature_names = joblib.load(
    "model/feature_names.pkl"
)


print("All files loaded successfully")


# Example input
data = {
    "Category": "Misconceptions",
    "Type": "Adversarial",
    "Model": "OpenAI",
    "ResponseLength": 80,
    "QuestionLength": 12,
    "ResponseCharacters": 500,
    "AverageWordLength": 7.0
}

df = pd.DataFrame([data])


# Encoding

df["Category"] = category_encoder.transform(
    df["Category"]
)

df["Type"] = type_encoder.transform(
    df["Type"]
)

df["Model"] = model_encoder.transform(
    df["Model"]
)


# Arrange features exactly like training

df = df[feature_names]


# Scaling

df_scaled = scaler.transform(df)


# Prediction

prediction = model.predict(df_scaled)

probability = model.predict_proba(df_scaled)


print("Prediction:", prediction[0])
print("Probability:", probability[0])