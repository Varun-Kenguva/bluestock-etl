# Data Dictionary

## 01_fund_master
This dataset contains the master information for all mutual fund schemes included in the project.

| Column             | Data Type | Description                             |
| ------------------ | --------- | --------------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier           |
| fund_house         | Text      | Name of the mutual fund company         |
| scheme_name        | Text      | Name of the scheme                      |
| category           | Text      | Primary fund category                   |
| sub_category       | Text      | Detailed fund category                  |
| plan               | Text      | Direct or Regular plan                  |
| launch_date        | Date      | Scheme launch date                      |
| benchmark          | Text      | Benchmark used for comparison           |
| expense_ratio_pct  | Float     | Expense ratio percentage                |
| exit_load_pct      | Float     | Exit load percentage                    |
| min_sip_amount     | Integer   | Minimum SIP amount                      |
| min_lumpsum_amount | Integer   | Minimum lump sum investment             |
| fund_manager       | Text      | Fund manager responsible for the scheme |
| risk_category      | Text      | Risk classification of the scheme       |
| sebi_category_code | Text      | SEBI category code                      |

## 02_nav_history

Stores the historical Net Asset Value (NAV) of mutual fund schemes across different dates.

## 03_aum_by_fund_house

Provides Assets Under Management (AUM) information for different fund houses over time.

## 04_monthly_sip_inflows

Tracks monthly SIP inflows, SIP assets under management, active SIP accounts, and yearly growth trends.

## 05_category_inflows

Shows monthly net inflows and outflows across different mutual fund categories.

## 06_industry_folio_count

Provides industry-wide folio statistics across equity, debt, hybrid, and other fund categories.

## 07_scheme_performance

Contains return metrics, risk measures, benchmark performance, and expense ratios for mutual fund schemes.

## 08_investor_transactions

Includes investor transaction records such as SIP, Lumpsum, and Redemption transactions along with demographic and KYC details.

## 09_portfolio_holdings

Contains portfolio holdings, sector allocation, stock weights, and market values for different schemes.

## 10_benchmark_indices

Stores benchmark index closing values used for performance comparison and analysis.
