import pandas as pd
import joblib

from feature_extraction import extract_features


MODEL_PATH = "model/random_forest.pkl"
SCALER_PATH = "model/scaler.pkl"

CATEGORY_ENCODER_PATH = "model/category_encoder.pkl"
TYPE_ENCODER_PATH = "model/type_encoder.pkl"
MODEL_ENCODER_PATH = "model/model_encoder.pkl"

FEATURE_NAMES_PATH = "model/feature_names.pkl"


classifier = joblib.load(
    MODEL_PATH
)

scaler = joblib.load(
    SCALER_PATH
)

category_encoder = joblib.load(
    CATEGORY_ENCODER_PATH
)

type_encoder = joblib.load(
    TYPE_ENCODER_PATH
)

model_encoder = joblib.load(
    MODEL_ENCODER_PATH
)


# Loading the feature order

feature_names = joblib.load(
    FEATURE_NAMES_PATH
)

#prediction function
def predict_hallucination(
        question,
        response,
        category,
        response_type,
        model_name
):


#extarcting features

    features = extract_features(

        question=question,

        response=response,

        category=category,

        response_type=response_type,

        model_name=model_name

    )


    df = pd.DataFrame(
        [features]
    )

#encoding categorical features

    df["Category"] = category_encoder.transform(
        df["Category"]
    )


    df["Type"] = type_encoder.transform(
        df["Type"]
    )


    df["Model"] = model_encoder.transform(
        df["Model"]
    )

    #arranging features in the same order as in the training stage
    df = df[
        feature_names
    ]

    df_scaled = scaler.transform(df)

    df_scaled = pd.DataFrame(
    df_scaled,
    columns=feature_names
    )


    prediction = classifier.predict(
    df_scaled
    )[0]


    probability = classifier.predict_proba(
    df_scaled
    )[0]



    confidence = max(probability)

#converting the output

    if prediction == 1:

        result = "Hallucinated"

    else:

        result = "Non-Hallucinated"



    return result, round(confidence*100,2)


