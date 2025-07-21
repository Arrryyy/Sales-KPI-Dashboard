import streamlit as st

def render_summary_cards(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Profit", f"${total_profit:,.2f}")