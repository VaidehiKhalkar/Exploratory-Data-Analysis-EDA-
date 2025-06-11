import streamlit as st
import pandas as pd
import numpy as np

# ── Page Configuration ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🚗 Car Dashboard",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS for KPI Cards ─────────────────────────────────────────────────────
st.markdown("""
<style>
div[data-testid="metric-container"] {
    background-color: #f5f5f5;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
}
div[data-testid="metric-container"] > label {
    font-size: 1rem;
    font-weight: 600;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# ── Load Built-In Dataset from GitHub ─────────────────────────────────────────────
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/usedcars.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# ── Sidebar Filtering ──────────────────────────────────────────────────────────────
st.sidebar.header("🔍 Filter Data")
df_filtered = df.copy()

# Categorical filters
cats = df_filtered.select_dtypes(include="object").columns
for col in cats:
    vals = st.sidebar.multiselect(col, options=df_filtered[col].unique(), default=df_filtered[col].unique())
    df_filtered = df_filtered[df_filtered[col].isin(vals)]

# Numeric filters
nums = df_filtered.select_dtypes(include=np.number).columns
for col in ["year", "price", "mileage"]:
    if col in nums:
        mi, ma = float(df_filtered[col].min()), float(df_filtered[col].max())
        low, high = st.sidebar.slider(f"{col} range", mi, ma, (mi, ma))
        df_filtered = df_filtered[(df_filtered[col] >= low) & (df_filtered[col] <= high)]

st.sidebar.markdown("---")

# ── Header & KPIs ────────────────────────────────────────────────────────────────
st.title("🚗 Used Cars EDA Dashboard")

col1, col2, col3, col4 = st.columns(4, gap="large")
col1.metric("Total Records", f"{len(df_filtered):,}")
if "price" in nums:
    col2.metric("Average Price", f"${df_filtered['price'].mean():,.0f}")
if "mileage" in nums:
    col3.metric("Average Mileage", f"{df_filtered['mileage'].mean():,.0f} mi")
if "year" in nums:
    col4.metric("Newest Model Year", f"{int(df_filtered['year'].max())}")

st.markdown("---")

# ── Native Streamlit Charts ──────────────────────────────────────────────────────
st.subheader("📊 Visual Exploration")
c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.write(f"### Cars by Year")
    st.bar_chart(df_filtered["year"].value_counts().sort_index())

with c2:
    st.write("### Price Trend")
    st.line_chart(df_filtered.groupby("year")["price"].mean())

with c3:
    st.write("### Mileage Distribution")
    st.area_chart(df_filtered["mileage"].dropna())

st.markdown("---")

# ── Data Table and Map ─────────────────────────────────────────────────────────────
tabs = st.tabs(["📋 Data Table", "🗺️ Map View"])
with tabs[0]:
    st.dataframe(df_filtered.reset_index(drop=True), use_container_width=True, height=300)
with tabs[1]:
    st.info("🗺️ Map requires `latitude` & `longitude` columns.")

st.markdown("---")

# ── Detailed Stats & Export ───────────────────────────────────────────────────────
with st.expander("📉 Detailed Statistics"):
    st.write(df_filtered.describe())

csv_data = df_filtered.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Filtered Data", data=csv_data, file_name="filtered_cars.csv", mime="text/csv")

st.markdown("---")

# ── Progress & Celebration ────────────────────────────────────────────────────────
progress = st.progress(0)
for i in range(0, 101, 20):
    progress.progress(i)
progress.empty()
st.success("✅ Dashboard Ready!")
st.balloons()
