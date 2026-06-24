import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("=" * 60)
print("BLUESTOCK DATA CLEANING PIPELINE")
print("=" * 60)

# ==========================================================
# 01 NAV HISTORY
# ==========================================================

print("\nCleaning NAV History...")

nav = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED_PATH}/02_nav_history_cleaned.csv",
    index=False
)

print("Saved: 02_nav_history_cleaned.csv")

# ==========================================================
# 02 INVESTOR TRANSACTIONS
# ==========================================================

print("\nCleaning Investor Transactions...")

txn = pd.read_csv(
    f"{RAW_PATH}/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[txn["amount_inr"] > 0]

txn = txn[
    txn["kyc_status"].isin(
        ["Verified", "Pending"]
    )
]

txn.to_csv(
    f"{PROCESSED_PATH}/08_investor_transactions_cleaned.csv",
    index=False
)

print("Saved: 08_investor_transactions_cleaned.csv")

# ==========================================================
# 03 SCHEME PERFORMANCE
# ==========================================================

print("\nCleaning Scheme Performance...")

perf = pd.read_csv(
    f"{RAW_PATH}/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf[
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
]

perf.to_csv(
    f"{PROCESSED_PATH}/07_scheme_performance_cleaned.csv",
    index=False
)

print("Saved: 07_scheme_performance_cleaned.csv")

# ==========================================================
# COPY REMAINING DATASETS
# ==========================================================

print("\nProcessing Remaining Datasets...")

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining_files:

    df = pd.read_csv(
        f"{RAW_PATH}/{file}"
    )

    output_name = file.replace(
        ".csv",
        "_cleaned.csv"
    )

    df.to_csv(
        f"{PROCESSED_PATH}/{output_name}",
        index=False
    )

    print(f"Saved: {output_name}")

print("\nAll cleaned datasets generated successfully.")

print("\nSummary")
print("-" * 40)
print(f"NAV Records: {len(nav)}")
print(f"Transaction Records: {len(txn)}")
print(f"Performance Records: {len(perf)}")
print("Processed Files: 10")