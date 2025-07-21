import streamlit as st
import pandas as pd
import plotly.express as px

def render_category_pie(df):
    category_sales = df.groupby("Category")["Sales"].sum().reset_index()
    fig = px.pie(category_sales, values="Sales", names="Category", title="Sales Distribution by Category")
    st.plotly_chart(fig, use_container_width=True)