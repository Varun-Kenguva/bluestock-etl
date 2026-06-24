import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "dim_fund": "data/processed/01_fund_master_cleaned.csv",
    "fact_nav": "data/processed/02_nav_history_cleaned.csv",
    "fact_aum": "data/processed/03_aum_by_fund_house_cleaned.csv",
    "sip_inflows": "data/processed/04_monthly_sip_inflows_cleaned.csv",
    "category_inflows": "data/processed/05_category_inflows_cleaned.csv",
    "industry_folios": "data/processed/06_industry_folio_count_cleaned.csv",
    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "portfolio_holdings": "data/processed/09_portfolio_holdings_cleaned.csv",
    "benchmark_indices": "data/processed/10_benchmark_indices_cleaned.csv"
}

for table_name, file_path in files.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}: {len(df)} rows loaded"
    )

print("\nSQLite database created successfully.")