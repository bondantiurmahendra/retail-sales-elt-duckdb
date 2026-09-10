
-- dim_product.sql
-- Membuat tabel dimensi produk dengan agregasi harga rata-rata
CREATE OR REPLACE TABLE analytics.dim_product AS
SELECT 
    "Product Category" AS product_category,
    ROUND(AVG("Price per Unit"), 2) AS avg_price_per_unit,
    COUNT(DISTINCT "Transaction ID") AS total_transactions
FROM read_parquet('raw_retail_sales.parquet')
GROUP BY "Product Category";
