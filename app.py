from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from fastapi.responses import JSONResponse

import pandas as pd
from joblib import load

app = FastAPI()

# Load model

model= load('modell/model.joblib')

    


@app.get("/")
def read_root():
    return {"message": "Welcome to the electricity cost  prediction API!"} 
        
@app.get("/health")
def health_check():
    status = {
        "status": "ok",
        "model_loaded": model is not None,
    }
    return JSONResponse(content=status)

@app.post("/prediction")
def predict(gram: UserInput):
        
        

        # Include ONLY the features the model expects
        input_data = {
            "site area": gram.site_area,
            "structure type": gram.structure_type_numeric,
            "water consumption": gram.water_consumption,
            "recycling rate": gram.recycling_rate,
            "utilisation rate": gram.utilisation_rate,
            "air qality index": gram.air_quality_index,
            "issue reolution time": gram.issue_resolution_time,
            "resident count": gram.resident_count
        }
        df = pd.DataFrame([input_data])
        
        
      
        prediction = model.predict(df)[0]
        return {"electricity_cost":int(prediction)}
    