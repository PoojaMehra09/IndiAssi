import streamlit as st
import pandas as pd
from src.tabs import data_viz_tab, classification_tab, clustering_tab, association_tab, regression_tab

st.set_page_config(
    page_title="Hotel Booking Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/your-username/your-repo-name/main/hotel_bookings.csv")
    return df

df = load_data()

st.sidebar.title("Navigation")
tabs = ["Data Visualization", "Classification", "Clustering", "Association Rules", "Regression"]
choice = st.sidebar.radio("Go to", tabs)

if choice == "Data Visualization":
    data_viz_tab(df)
elif choice == "Classification":
    classification_tab(df)
elif choice == "Clustering":
    clustering_tab(df)
elif choice == "Association Rules":
    association_tab(df)
elif choice == "Regression":
    regression_tab(df)
