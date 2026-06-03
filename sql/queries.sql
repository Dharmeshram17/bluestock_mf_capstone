-- 1 Top 5 funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- 2 Average NAV per month

SELECT
substr(date,1,7) as month,
AVG(nav)

FROM fact_nav

GROUP BY month;


-- 3 Transaction Count by State

SELECT
state,
COUNT(*)

FROM fact_transactions

GROUP BY state

ORDER BY COUNT(*) DESC;


-- 4 Expense Ratio below 1%

SELECT
amfi_code,
expense_ratio_pct

FROM fact_performance

WHERE expense_ratio_pct <1;


-- 5 SIP Transactions Count

SELECT
COUNT(*)

FROM fact_transactions

WHERE transaction_type='SIP';


-- 6 Total Transactions

SELECT COUNT(*)

FROM fact_transactions;


-- 7 Maximum NAV

SELECT MAX(nav)

FROM fact_nav;


-- 8 Minimum NAV

SELECT MIN(nav)

FROM fact_nav;


-- 9 Average Expense Ratio

SELECT AVG(expense_ratio_pct)

FROM fact_performance;


-- 10 Funds Count by Category

SELECT
category,
COUNT(*)

FROM dim_fund

GROUP BY category;