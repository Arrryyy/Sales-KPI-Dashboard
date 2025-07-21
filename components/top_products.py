import streamlit as st
import pandas as pd

def render_top_products(df, top_n=10):
    top_products = df.groupby("Product Name")["Sales"].sum().reset_index()
    top_products = top_products.sort_values(by="Sales", ascending=False).head(top_n)

    st.subheader(f"Top {top_n} Products by Sales")
    st.dataframe(top_products, use_container_width=True)