
-- dim_customer.sql
-- Membuat tabel dimensi pelanggan dengan feature engineering (age_group)
CREATE OR REPLACE TABLE analytics.dim_customer AS
SELECT DISTINCT
    "Customer ID" AS customer_id,
    Gender AS gender,
    Age AS age,
    CASE 
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 50 THEN '35-49'
        ELSE '50+'
    END AS age_group
FROM read_parquet('raw_retail_sales.parquet');
