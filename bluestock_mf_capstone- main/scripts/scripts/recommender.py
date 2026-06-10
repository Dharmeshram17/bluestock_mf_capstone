import pandas as pd

scheme = pd.read_csv(
    "../Data/processed/scheme_performance_cleaned.csv"
)

risk_input = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

recommendations = (
    scheme[
        scheme["risk_grade"].str.contains(
            risk_input,
            case=False,
            na=False
        )
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
)

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ].head(3)
)