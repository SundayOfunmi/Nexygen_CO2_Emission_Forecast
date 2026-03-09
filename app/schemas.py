from pydantic import BaseModel
from typing import List


class ForecastItem(BaseModel):
    date: str
    value: float


class ForecastResponse(BaseModel):
    scope: str
    forecast: List[ForecastItem]


class ScenarioItem(BaseModel):
    date: str
    baseline: float
    reduction_5: float
    reduction_10: float


class ScenarioResponse(BaseModel):
    scenarios: List[ScenarioItem]

