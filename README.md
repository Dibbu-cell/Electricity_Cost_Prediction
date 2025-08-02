# ⚡ Electricity_Cost_Prediction_API
Welcome to the Electricity_Cost_Prediction_API. This project will predict monthly electricity costs for residential and commercial structures using GradientBoostingRegressor Machie Learning algorithm.  this API is designed to provide accurate predictions based on environmental and structural features.

---


## 🌐 Live API
**Base URL:** https://electricity-cost-api-m893.onrender.com/docs

---
## 📌 Endpoints
### . `GET /`
Welcome Page.

**Response:**
```json
{"message":"Welcome to the electricity cost  prediction API!"}
```

### . `GET /health`
This endpoint will assure you that your api is working fine and your model is loading properly.

**Response:**
```text
{
  "status": "ok",
  "model_loaded": true
}
```

### . `POST /prediction`
Submit the data according to model and get the output.

**Request Body**
```text
{
  "site_area": 100,
  "structure_type": "Mixed-use",
  "water_consumption": 10,
  "recycling_rate": 20,
  "utilisation_rate": 10,
  "air_quality_index": 80,
  "issue_resolution_time": 10,
  "resident_count": 19
}
```
**Response:**
```text
{
  "electricity_cost": 6130
}


```


---


## ▀▄▀▄▀▄ PROJECT OVERVIEW ▄▀▄▀▄▀

This project is more than just an API; it's a complete pipeline that includes:

. **Exploratory Data Analysis (EDA) and preprocessing** of  CSV data  
. **Training and evaluation** of a Machine Learning regression model  
. **FastAPI backend** for seamless predictions  
. **Live deployment** on Render  for global accessibility  


---
## 🧠 Model Features

The prediction model considers these key parameters:

| Feature Category       | Description                                                                 | Units/Values                     |
|------------------------|-----------------------------------------------------------------------------|----------------------------------|
| **Geospatial**         |                                                                             |                                  |
| `Site Area`            | Total area of the site                                                      | Square meters (m²)               |
| `Structure Type`       | Building classification                                                     | Residential/Commercial/Mixed-use  |
|                        |                                                                             |                                  |
| **Resource Usage**     |                                                                             |                                  |
| `Water Consumption`    | Monthly water usage                                                        | Liters (L)                       |
| `Recycling Rate`       | Percentage of waste recycled                                               | Percentage (%)                   |
| `Utilisation Rate`     | Percentage of resource utilization                                         | Percentage (%)                   |
|                        |                                                                             |                                  |
| **Environmental**      |                                                                             |                                  |
| `Air Quality Index`    | Measure of air pollution (higher = worse air quality)                      | 0-500 scale                      |
|                        |                                                                             |                                  |
| **Operational**        |                                                                             |                                  |
| `Issue Resolution Time`| Average time to resolve maintenance issues                                 | Hours (h)                        |
| `Resident Count`       | Number of regular occupants                                                | Count                            |
---
## 📈 Model Performance

### 📊 Evaluation Metrics
| Metric          | Score     | Interpretation                     |
|-----------------|-----------|------------------------------------|
| **R² Score**    | 0.96      | Explains 96% of cost variance      |
| **MSE**         | 46,886.6  | Mean squared error                 |
| **MAE**         | 173.38    | Mean absolute error in cost units  |





---
## ☁ Deployment on Render
The API is deployed on Render.
✅ FastAPI app served with Uvicorn  
✅ Automated deployment using **docker image**

✅ Accessible at: https://electricity-cost-api-m893.onrender.com/docs


---

📁 **Project Structure**



```text
ElectricityCostPrediction/
│
├── model/
│   ├── electricity_cost_dataset.csv  # Dataset used for training
│   └── model.joblib                 # Trained ML model (serialized)
│
├── schema/
│   └── user_input.py                # Pydantic models for data validation
│
├── app.py                           # FastAPI application entry point
├── Dockerfile                       # Containerization configuration
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── frontend.py                      # Optional frontend interface
└── electricity.ipynb                # Jupyter notebook (EDA/feature engineering/model training)

```
---

I hope you find this electricity cost prediction api good enough .  If  you have any doubt feel free to ask me through mail ** aryansingh962149@gmail.com**



