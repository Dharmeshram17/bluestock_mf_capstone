import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

print("Total CSV files found:", len(csv_files))

for file in csv_files:
    print("\n" + "="*50)
    print("File Name:", file.name)
    df = pd.read_csv(file)
    print("\nShape:")
    print(df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")
print("="*50)
print("FUND MASTER ANALYSIS")
print("="*50)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nColumns:")
print(fund_master.columns)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())


print("\n")
print("="*50)
print("AMFI CODE VALIDATION")
print("="*50)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))

print("Total NAV Codes:", len(nav_codes))

print("Missing Codes:")

print(missing_codes)

if len(missing_codes)==0:
    print("All AMFI codes validated successfully")
else:
    print("Some AMFI codes are missing")





