from fastapi import FastAPI
from app.schema import ElectricityInput
import pandas as pd
import joblib


def lowercase_columns(df):
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].str.lower()
    return df

# Register it before loading the model
import __main__
__main__.lowercase_columns = lowercase_columns

app = FastAPI()

# Load trained model
model = joblib.load("app/model.joblib")

@app.get("/")
def home():
    return {"message": "Electricity Cost Prediction API is running."}

@app.post("/predict")
def predict(data: ElectricityInput):
    input_data = pd.DataFrame([data.dict()])

    # Rename to match training
    input_data.columns = [
        'site area', 'structure type', 'water consumption', 'recycling rate',
        'utilisation rate', 'air qality index', 'issue reolution time', 'resident count'
    ]

    # Lowercase object columns
    input_data = input_data.apply(lambda col: col.str.lower() if col.dtypes == 'object' else col)

    prediction = model.predict(input_data)[0]

    return {"predicted_cost": round(prediction, 2)}
