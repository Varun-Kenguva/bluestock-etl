-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
-- 2. Average NAV per Month
SELECT
strftime('%Y-%m', nav_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
-- 3. SIP YoY Growth

SELECT
month,
yoy_growth_pct
FROM sip_inflows
ORDER BY month;
-- 4. Transactions by State
SELECT
state,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;
-- 5. Funds with Expense Ratio < 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;
-- 6. Top 5 Fund Houses by Number of Schemes
SELECT
fund_house,
COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY fund_house
ORDER BY scheme_count DESC
LIMIT 5;
-- 7. Average Transaction Amount by Transaction Type
SELECT
transaction_type,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;
-- 8. Total AUM by Fund House
SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;
-- 9. Distribution of Investors by KYC Status
SELECT
kyc_status,
COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status;
-- 10. Top 10 Most Held Stocks
SELECT
stock_name,
COUNT(*) AS fund_count
FROM portfolio_holdings
GROUP BY stock_name
ORDER BY fund_count DESC
LIMIT 10;
