# 🦆 Retail Sales ELT Pipeline: Local-First Data Lakehouse with DuckDB

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![DuckDB](https://img.shields.io/badge/DuckDB-OLAP-orange.svg)
![Parquet](https://img.shields.io/badge/Storage-Apache%20Parquet-green.svg)
![SQL](https://img.shields.io/badge/SQL-ANSI%20Standard-yellow.svg)

## 📌 Project Overview
Proyek ini mendemonstrasikan pembangunan **End-to-End ELT (Extract, Load, Transform) Pipeline** menggunakan dataset Retail Sales dari Kaggle. Alih-alih menggunakan infrastruktur cloud yang berat, proyek ini mengadopsi arsitektur **Local-First Data Lakehouse** yang modern, memanfaatkan format kolom (Parquet) dan mesin analitik in-process (DuckDB) untuk memproses dan memodelkan data menjadi **Star Schema**.

Proyek ini menyoroti kemampuan dalam:
- Ingesting data secara programatik dari sumber eksternal (Kaggle).
- Konversi format data mentah (CSV) ke format analitik yang efisien (Parquet).
- Dimensional Modeling (Star Schema) menggunakan SQL.
- Feature Engineering langsung di dalam layer database.

---

## 🏗️ Architecture Diagram

```mermaid
graph LR
    A[Kaggle API] -->|1. Extract| B(Python / kagglehub)
    B -->|2. Load as CSV| C[(Local Storage)]
    C -->|3. Convert| D[(Apache Parquet / Data Lake)]
    D -->|4. Read & Transform| E{DuckDB Engine}
    E -->|5. Create Star Schema| F[(analytics.dim_customer)]
    E -->|5. Create Star Schema| G[(analytics.dim_product)]
    E -->|5. Create Star Schema| H[(analytics.fact_sales)]
    H -.->|Join for Analytics| I[Business Insights]

```
### 📊 Menjalankan Dashboard Visualisasi
Setelah pipeline selesai dijalankan dan file `retail_warehouse.db` terbentuk, Anda dapat memvisualisasikan datanya:
1. Install dependencies: `pip install -r requirements.txt`
2. Jalankan aplikasi Streamlit: `streamlit run app/app.py`
3. Buka browser di `http://localhost:8501`
