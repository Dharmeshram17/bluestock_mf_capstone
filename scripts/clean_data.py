import pandas as pd

performance = pd.read_csv(
    "Data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

anomalies = performance[
    (
        performance["expense_ratio_pct"] < 0.1
    )
    |
    (
        performance["expense_ratio_pct"] > 2.5
    )
]

print("\nExpense Ratio Anomalies:\n")

print(
    anomalies[
        ["scheme_name","expense_ratio_pct"]
    ]
)

print("\nNull Values in Returns:\n")

print(
    performance[
        return_cols
    ].isnull().sum()
)

print("\nRows After Cleaning:\n")

print(
    performance.shape
)

performance.to_csv(
    "Data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nSaved Successfully")