import streamlit as st
import pandas as pd

@st.cache  
def load_data(file_path):
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    df.dropna(how="all", inplace=True)
    return df