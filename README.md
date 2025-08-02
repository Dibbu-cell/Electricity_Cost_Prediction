# ⚡ Electricity_Cost_Prediction_API
Welcome to the Electricity_Cost_Prediction_API. This project will predict monthly electricity costs for residential and commercial structures using GradientBoostingRegressor Machie Learning algorithm.  this API is designed to provide accurate predictions based on environmental and structural features.


## 🌐 Live API
**Base URL:** https://electricity-cost-api-m893.onrender.com/docs





📁 **Project Structure**

## 📁 Project Structure

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
