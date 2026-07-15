import joblib

print("Loading random forest...")

model = joblib.load(
    "model/random_forest.pkl"
)

print("Loaded successfully")
print(type(model))
print(model.n_estimators)