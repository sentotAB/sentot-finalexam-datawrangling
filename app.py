import streamlit as st
import pandas as pd

st.title("Dashboard DataFrame Sentot UAS Data Wrangling")
df = pd.read_csv("netflix_clean.csv")
st.write(df.head())
