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



