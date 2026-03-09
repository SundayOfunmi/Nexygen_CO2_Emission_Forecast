import pandas as pd

# Load datasets
df = pd.read_csv("data/curated_scope_wide.csv", parse_dates=["YearMonth"])
forecast_df = pd.read_csv("data/forecast_output.csv", parse_dates=["ds"])


def get_historical_data():
    return df.to_dict(orient="records")


def get_forecast(scope: str):
    
    col = scope

    result = forecast_df[["ds", col]].dropna()

    return {
        "scope": scope,
        "forecast": [
            {"date": str(row["ds"]), "value": row[col]}
            for _, row in result.iterrows()
        ]
    }


def get_scenarios():

    base = forecast_df.copy()

    base["reduction_5"] = base["SCOPE 1"] * 0.95
    base["reduction_10"] = base["SCOPE 1"] * 0.90

    return {
        "scenarios": [
            {
                "date": str(row["ds"]),
                "baseline": row["SCOPE 1"],
                "reduction_5": row["reduction_5"],
                "reduction_10": row["reduction_10"]
            }
            for _, row in base.iterrows()
        ]
    }


def calculate_target_gap():

    df["gap"] = df["SCOPE 1"] - df["SCOPE 2"]

    return df[["YearMonth", "gap"]].to_dict(orient="records")

