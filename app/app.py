# app/app.py
import streamlit as st
import duckdb
import plotly.express as px
import os

# Konfigurasi halaman
st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")
st.title("📊 Retail Sales Analytics Dashboard")

# Koneksi ke DuckDB (Perhatikan '../' karena file .db ada di folder root/induk)
db_path = os.path.join(os.path.dirname(__file__), '..', 'retail_warehouse.db')
con = duckdb.connect(db_path)

try:
    # Query 1: Revenue per Kategori
    df_revenue = con.sql("""
        SELECT product_category, SUM(total_amount) as total_revenue
        FROM analytics.fact_sales
        GROUP BY product_category
        ORDER BY total_revenue DESC
    """).df()

    # Query 2: Demografi Pembeli
    df_demo = con.sql("""
        SELECT c.age_group, c.gender, COUNT(f.transaction_id) as total_tx
        FROM analytics.fact_sales f
        JOIN analytics.dim_customer c ON f.customer_id = c.customer_id
        GROUP BY c.age_group, c.gender
    """).df()

    # Tampilkan Visualisasi
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💰 Total Revenue per Product Category")
        fig1 = px.bar(df_revenue, x='product_category', y='total_revenue', color='product_category', labels={'total_revenue': 'Revenue (IDR)'})
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("👥 Transaksi berdasarkan Demografi")
        fig2 = px.bar(df_demo, x='age_group', y='total_tx', color='gender', barmode='group', labels={'total_tx': 'Jumlah Transaksi'})
        st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Error membaca database: {e}")
    st.info("Pastikan Anda sudah menjalankan notebook untuk membuat file 'retail_warehouse.db'")
finally:
    con.close()