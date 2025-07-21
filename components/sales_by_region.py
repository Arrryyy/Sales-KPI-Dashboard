import streamlit as st
import pandas as pd
import altair as alt

def render_sales_by_region(df):
    grouped = df.groupby("Region")["Sales"].sum().reset_index()

    chart = alt.Chart(grouped).mark_bar().encode(
        x=alt.X("Region:N", sort="-y"),
        y="Sales:Q",
        tooltip=["Region", "Sales"]
    ).properties(title="Sales by Region")

    st.altair_chart(chart, use_container_width=True)