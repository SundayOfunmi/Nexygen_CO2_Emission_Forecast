from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
import pandas as pd

from app.schemas import ForecastResponse, ScenarioResponse
from app.auth import verify_token
from app.services import (
    get_historical_data,
    get_forecast,
    get_scenarios,
    calculate_target_gap
)

app = FastAPI(
    title="Carbon Emissions API",
    description="API for emissions analytics, forecasting, and scenarios",
    version="1.0.0"
)

security = HTTPBearer()

# ============================
# Health Check
# ============================
@app.get("/health")
def health():
    return {"status": "ok"}


# ============================
# Historical Data
# ============================
@app.get("/historical")
def historical_data(token=Depends(verify_token)):
    return get_historical_data()


# ============================
# Forecast Endpoint
# ============================
@app.get("/forecast", response_model=ForecastResponse)
def forecast(scope: str, token=Depends(verify_token)):
    
    if scope not in ["SCOPE 1", "SCOPE 2"]:
        raise HTTPException(status_code=400, detail="Invalid scope")

    return get_forecast(scope)


# ============================
# Scenario Analysis
# ============================
@app.get("/scenarios", response_model=ScenarioResponse)
def scenarios(token=Depends(verify_token)):
    return get_scenarios()


# ============================
# Target Gap
# ============================
@app.get("/target-gap")
def target_gap(token=Depends(verify_token)):
    return calculate_target_gap()

