import streamlit as st
import pandas as pd
import altair as alt

def render_order_delay_chart(df):
    df = df.copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Delay (Days)"] = (df["Ship Date"] - df["Order Date"]).dt.days

    delay_data = df.groupby("Region")["Delay (Days)"].mean().reset_index()

    chart = alt.Chart(delay_data).mark_bar().encode(
        x="Region:N",
        y="Delay (Days):Q",
        tooltip=["Region", "Delay (Days)"]
    ).properties(title="Average Order Processing Delay by Region")

    st.altair_chart(chart, use_container_width=True)