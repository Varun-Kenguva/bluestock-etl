import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
csv_files = sorted(raw_path.glob("*.csv"))
print(f"\nFound {len(csv_files)} datasets\n")

for file in csv_files:
    print("=" * 70)
    print(f"Dataset: {file.name}")
    try:
        df = pd.read_csv(file)
        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\n")
    except Exception as e:
        print(f"Error reading {file.name}: {e}")


print("\n" + "=" * 70)
print("FUND MASTER ANALYSIS")
print("=" * 70)
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())


nav_history = pd.read_csv("data/raw/02_nav_history.csv")
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\n" + "=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

if len(missing_codes) == 0:
    print("All AMFI codes from fund_master exist in nav_history.")
else:
    print(f"Missing AMFI codes: {missing_codes}")


print("\n" + "=" * 70)
print("DATA QUALITY SUMMARY")
print("=" * 70)
print(f"Total Funds: {len(fund_master)}")
print(f"Fund Houses: {fund_master['fund_house'].nunique()}")
print(f"Categories: {fund_master['category'].nunique()}")
print(f"Sub Categories: {fund_master['sub_category'].nunique()}")
print(f"Risk Categories: {fund_master['risk_category'].nunique()}")