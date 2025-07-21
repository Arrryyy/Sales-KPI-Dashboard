import streamlit as st

st.set_page_config(page_title="Sales KPI Dashboard", layout="wide")
import pandas as pd
from components.summary_card import render_summary_cards
from components.sales_chart import render_sales_chart
from utils.data_loader import load_data
from components.sales_by_region import render_sales_by_region
from components.top_products import render_top_products
from components.category_pie import render_category_pie
from components.order_delay_chart import render_order_delay_chart
df = load_data("Data/Global_Superstore2.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
st.title(" Sales KPI Dashboard")

render_summary_cards(df)
render_sales_chart(df)
render_sales_by_region(df)
render_top_products(df) 
render_category_pie(df)  
render_order_delay_chart(df)