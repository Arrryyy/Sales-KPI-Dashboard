import streamlit as st
import pandas as pd
import altair as alt

def render_sales_chart(df):
    sales_by_month = df.copy()
    sales_by_month["Order Date"] = pd.to_datetime(sales_by_month["Order Date"])
    sales_by_month["Month"] = sales_by_month["Order Date"].dt.to_period("M").dt.to_timestamp()
    grouped = sales_by_month.groupby("Month")["Sales"].sum().reset_index()

    chart = alt.Chart(grouped).mark_line(point=True).encode(
        x="Month:T",
        y="Sales:Q",
        tooltip=["Month", "Sales"]
    ).properties(title="Monthly Sales Trend")

    st.altair_chart(chart, use_container_width=True)