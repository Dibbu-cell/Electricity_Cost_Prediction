# ⚡ Electricity_Cost_Prediction_API
Welcome to the Electricity_Cost_Prediction_API. This project will predict monthly electricity costs for residential and commercial structures using GradientBoostingRegressor Machie Learning algorithm.  this API is designed to provide accurate predictions based on environmental and structural features.


## 🌐 Live API
**Base URL:** https://electricity-cost-api-m893.onrender.com/docs






📁 Project Structure

ElectricityCostPrediction/
│
├── modell/
│   ├── electricity_cost_dataset.csv           # FastAPI app
│   ├── model.joblib           # Trained ML model     
│           
│
├── schema/
│    ├── user_input.py      # Pydantic model for validation
├──app.py                   # FastAPI app
├── Dockerfile              # process of making docker image
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├──frontend.py              # you can connect it with deployed api
├──electricity.ipynb        # all process like feature engneering,training ,testing 
