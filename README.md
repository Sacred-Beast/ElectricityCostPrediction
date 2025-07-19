# ⚡ Electricity Cost Prediction API

Welcome to the **Electricity Cost Prediction API**! This project is your gateway to predicting monthly electricity costs for residential and commercial structures using cutting-edge Machine Learning techniques. Whether you're a homeowner, business owner, or data enthusiast, this API is designed to provide accurate predictions based on environmental and structural features.

---

## 🌐 Live API

🔗 **Base URL**: [https://electricity-cost-api.onrender.com](https://electricity-cost-api.onrender.com)

### Endpoints

- **GET /**  
  A simple health check to ensure the API is up and running.  
  ➤ Response:  
  ```json
  {"message": "Electricity Cost Prediction API is running."}
  ```

- **POST /predict**  
  Submit your data and get a prediction for monthly electricity costs.  
  ➤ Request Body (JSON):

  ```json
  {
    "site_area": 1500,
    "structure_type": "commercial",
    "water_consumption": 600,
    "recycling_rate": 50,
    "utilisation_rate": 80,
    "air_quality_index": 45,
    "issue_resolution_time": 12,
    "resident_count": 30
  }
  ```

  ➤ Response:

  ```json
  {
    "predicted_cost": 1894
  }
  ```

---

## 📦 Project Overview

This project is more than just an API; it's a complete pipeline that includes:

* ✅ Exploratory Data Analysis (EDA) and preprocessing of structured CSV data
* ✅ Training and evaluation of a Machine Learning regression model
* ✅ A FastAPI backend for seamless predictions
* ✅ Live deployment on **Render** for global accessibility

---

## 🧠 Features Used

The prediction model considers the following features:

* **Site Area**: Total area of the site in square meters
* **Structure Type**: Residential or commercial (categorical)
* **Water Consumption**: Monthly water usage in liters
* **Recycling Rate**: Percentage of waste recycled
* **Utilisation Rate**: Percentage of resource utilization
* **Air Quality Index**: Measure of air pollution
* **Issue Resolution Time**: Average time to resolve issues (in hours)
* **Resident Count**: Number of residents or occupants

---

## 📁 Project Structure

Here's how the project is organized:

```
ElectricityCostPrediction/
│
├── app/
│   ├── main.py             # FastAPI app
│   ├── schema.py           # Pydantic model for validation
│   └── model.joblib        # Trained ML model
│
├── data/
│   └── electricity_cost.csv
│
├── notebooks/
│   └── EDA_and_Model.ipynb # EDA + model training notebook
│
├── render.yaml             # Render deployment config
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Local Setup

Want to run the API locally? Follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sacred-Beast/ElectricityCostPrediction.git
   cd ElectricityCostPrediction
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API Locally**

   ```bash
   uvicorn app.main:app --reload
   ```

5. Open your browser and navigate to:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📈 Model Performance

Our prediction model is powered by a **Random Forest Regressor**. Here's how it performs:

* 🔹 **RMSE**: 486.21
* 🔹 **MAE**: 412.78
* 🔹 **R² Score**: 0.89

These metrics demonstrate the model's accuracy and reliability in predicting electricity costs.

---

## ☁ Deployment on Render

The API is deployed on **Render**, ensuring high availability and scalability. Key highlights:

* ✅ FastAPI app served with **Uvicorn**
* ✅ Automated deployment using `render.yaml`
* ✅ Accessible at: [https://electricity-cost-api.onrender.com](https://electricity-cost-api.onrender.com)

---

## 📄 License

This project is open-source and licensed under the **MIT License**. Feel free to use, modify, and share!  
© 2025 [Sacred Beast](https://github.com/Sacred-Beast)

---

Thank you for exploring the Electricity Cost Prediction API! If you have any questions or feedback, feel free to reach out. Happy predicting! 🚀
