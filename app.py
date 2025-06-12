import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Used Car Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load and Preprocess Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("car_data.csv")
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["Price"], inplace=True)
    
    # Clean Engine, Mileage, Power if present
    if "Engine" in df.columns:
        df["Engine"] = df["Engine"].str.extract(r'(\d+)').astype(float)
    if "Power" in df.columns:
        df["Power"] = df["Power"].str.extract(r'(\d+.\d+)').astype(float)
    if "Mileage" in df.columns:
        df["Mileage"] = df["Mileage"].str.extract(r'(\d+.\d+)').astype(float)
    
    df["Price"] = df["Price"].astype(float)
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("🔎 Filters")
brand_filter = st.sidebar.selectbox("Select Brand", ["All"] + sorted(df["Name"].dropna().str.split().str[0].unique()))
fuel_filter = st.sidebar.multiselect("Fuel Type", options=df["Fuel_Type"].dropna().unique(), default=df["Fuel_Type"].dropna().unique())
trans_filter = st.sidebar.multiselect("Transmission", options=df["Transmission"].dropna().unique(), default=df["Transmission"].dropna().unique())

filtered_df = df.copy()
if brand_filter != "All":
    filtered_df = filtered_df[filtered_df["Name"].str.startswith(brand_filter)]
filtered_df = filtered_df[
    (filtered_df["Fuel_Type"].isin(fuel_filter)) &
    (filtered_df["Transmission"].isin(trans_filter))
]

# --- Dashboard Title ---
st.title("🚗 Used Car Analysis Dashboard")
st.markdown("""
Interactive dashboard to explore used car listings, pricing trends, and market features.
""")

# --- Tabs ---
tabs = st.tabs(["📊 Overview", "📈 Trends", "📎 Correlation Matrix", "📋 Data Table"])

# --- Overview Tab ---
with tabs[0]:
    st.markdown("### 📊 Key Metrics")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Listings", len(filtered_df))
    kpi2.metric("Average Price", f"₹{filtered_df['Price'].mean():,.0f}")
    kpi3.metric("Most Common Brand", filtered_df["Name"].str.split().str[0].mode()[0])
    kpi4.metric("Popular Fuel Type", filtered_df["Fuel_Type"].mode()[0])

    st.markdown("---")
    sum1, sum2 = st.columns(2)
    sum1.success(f"Transmission Mode: {filtered_df['Transmission'].mode()[0]}")
    if "Owner_Type" in filtered_df.columns:
        sum2.info(f"Most Common Ownership: {filtered_df['Owner_Type'].mode()[0]}")

# --- Trends Tab ---
with tabs[1]:
    st.subheader("💵 Price Distribution by Fuel Type")
    fuel_price = filtered_df.groupby("Fuel_Type")["Price"].mean()
    st.bar_chart(fuel_price)

    st.markdown("---")
    st.subheader("⚙️ Transmission Split")
    trans_counts = filtered_df["Transmission"].value_counts()
    st.bar_chart(trans_counts)

    st.markdown("---")
    if "Year" in filtered_df.columns:
        st.subheader("📆 Year-wise Listing Count")
        year_dist = filtered_df["Year"].value_counts().sort_index()
        st.line_chart(year_dist)

# --- Correlation Matrix Tab ---
with tabs[2]:
    st.subheader("📎 Correlation Matrix")
    numeric_cols = filtered_df.select_dtypes(include=["int64", "float64"])
    corr_matrix = numeric_cols.corr().round(2)
    st.dataframe(corr_matrix)

# --- Data Table Tab ---
with tabs[3]:
    st.subheader("📋 Filtered Data Table")
    page_size = 50
    total_rows = len(filtered_df)
    total_pages = (total_rows - 1) // page_size + 1
    current_page = st.number_input("Page", min_value=1, max_value=total_pages, step=1)
    start = (current_page - 1) * page_size
    end = start + page_size
    st.dataframe(filtered_df.iloc[start:end].reset_index(drop=True))

# --- Footer ---
st.markdown("---")
st.markdown("📘 Powered by Streamlit | Data: Used Car Listings | Visualization: Streamlit-native components only")
