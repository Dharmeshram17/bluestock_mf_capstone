# Data Dictionary

## Fund Master

| Column | Data Type | Description |
|-------|-------|-------|
| amfi_code | Integer | Unique fund identifier |
| scheme_name | Text | Name of mutual fund scheme |
| fund_house | Text | Mutual fund company |
| category | Text | Fund category |

Source: 01_fund_master.csv


## NAV History

| Column | Data Type | Description |
|-------|-------|-------|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

Source: 02_nav_history.csv


## Investor Transactions

| Column | Data Type | Description |
|-------|-------|-------|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction amount |
| kyc_status | Text | Verification status |

Source: 08_investor_transactions.csv


## Scheme Performance

| Column | Data Type | Description |
|-------|-------|-------|
| return_1yr_pct | Float | One year return |
| return_3yr_pct | Float | Three year return |
| return_5yr_pct | Float | Five year return |
| expense_ratio_pct | Float | Expense ratio percentage |

Source: 07_scheme_performance.csv