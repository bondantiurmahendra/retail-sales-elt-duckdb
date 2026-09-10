
-- fact_sales.sql
-- Membuat tabel fakta transaksi yang menghubungkan ke dimensi
CREATE OR REPLACE TABLE analytics.fact_sales AS
SELECT
    "Transaction ID" AS transaction_id,
    CAST("Date" AS DATE) AS sale_date,
    "Customer ID" AS customer_id,
    "Product Category" AS product_category,
    Quantity AS quantity,
    "Price per Unit" AS price_per_unit,
    "Total Amount" AS total_amount
FROM read_parquet('raw_retail_sales.parquet');
