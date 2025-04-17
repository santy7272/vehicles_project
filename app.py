import streamlit as st
import pandas as pd
import plotly.express as px

# 1. App title
st.header("🚗 Used Cars Analysis in the U.S.")

# 2. Load dataset
df = pd.read_csv("vehicles_us.csv")

# reviewer note -
df["model_year"] = df["model_year"].fillna(df["model_year"].median())
df["cylinders"] = df.groupby("model")["cylinders"].transform(lambda x: x.fillna(x.median()))
df["odometer"] = df.groupby("model")["odometer"].transform(lambda x: x.fillna(x.median()))
df["paint_color"] = df["paint_color"].fillna("Unknown")


# 3. Checkbox to display the first few rows
if st.checkbox("📋 Show first rows of the dataset"):
    st.write(df.head())

# 4. Histogram (Price distribution)
st.subheader("📊 Price Distribution")
fig_hist = px.histogram(df, x="price", nbins=50, title="Vehicle Price Distribution")
st.plotly_chart(fig_hist)

# 5. Checkbox to filter only vehicles in 'good' condition
filter_excellent = st.checkbox("Show only vehicles in 'good condition")

# 6. Apply filter to the DataFrame based on checkbox
if filter_excellent:
    df = df[df["condition"] == "good"]

# 7. Scatter plot: Price vs Model Year
st.subheader("📈 Price vs Model Year")
fig_scatter = px.scatter(
    df,
    x="model_year",
    y="price",
    color="condition",
    title="Relationship Between Price and Model Year"
)
st.plotly_chart(fig_scatter)

# 8. Histogram: Price distribution of Jeep Wrangler
st.subheader("🚙 Price Distribution: Jeep Wrangler")

# My favourite car: Jeep
wrangler_df = df[df['model'].str.lower().str.contains('wrangler')]

# Checking if there are any Wrangler listings before plotting
if not wrangler_df.empty:
    fig_wrangler = px.histogram(
        wrangler_df,
        x="price",
        nbins=30,
        title="Price Distribution of Jeep Wrangler (my favourite)"
    )
    st.plotly_chart(fig_wrangler)
else:
    st.write("No Jeep Wrangler listings found in the dataset.")

# 9. Histogram: Price distribution by fuel type
st.subheader("⛽ Price Distribution by Fuel Type")

fig_fuel = px.histogram(
    df,
    x="price",
    color="fuel",
    nbins=50,
    title="Vehicle Price Distribution by Fuel Type",
    labels={"fuel": "Fuel Type", "price": "Price"},
    barmode="overlay"  
)

st.plotly_chart(fig_fuel)
