import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Interactive Happiness Dashboard")

    # Load data
    try:
        data_2019 = pd.read_csv("data/happiness/2019.csv")
    except FileNotFoundError:
        st.error("Error: 2019.csv not found. Please make sure the data file is in the correct directory.")
        return

    # Interactive Map
    st.header("World Happiness Map (2019)")
    
    # Check if 'Country or region' and 'Score' columns exist
    if 'Country or region' not in data_2019.columns or 'Score' not in data_2019.columns:
        st.error("Error: 'Country or region' or 'Score' column not found in the 2019 data.")
        return

    try:
        fig = px.choropleth(
            data_2019,
            locations="Country or region",
            locationmode="country names",
            color="Score",
            hover_name="Country or region",
            color_continuous_scale=px.colors.sequential.Plasma,
            title="Happiness Score by Country",
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"An error occurred while creating the map: {e}")

    # Country specific data
    st.header("Country Specific Data")
    country = st.selectbox("Select a Country", data_2019["Country or region"])

    if country:
        st.subheader(f"Key Indicators for {country}")
        country_data = data_2019[data_2019["Country or region"] == country].iloc[0]
        st.write(f"**Happiness Score:** {country_data['Score']}")
        st.write(f"**GDP per capita:** {country_data['GDP per capita']}")
        st.write(f"**Social support:** {country_data['Social support']}")
        st.write(f"**Healthy life expectancy:** {country_data['Healthy life expectancy']}")
        st.write(f"**Freedom to make life choices:** {country_data['Freedom to make life choices']}")
        st.write(f"**Generosity:** {country_data['Generosity']}")
        st.write(f"**Perceptions of corruption:** {country_data['Perceptions of corruption']}")

    # AI-generated explanatory text
    st.header("AI-Generated Explanations")
    st.write("This dashboard provides an interactive exploration of the World Happiness Report data from 2019. The map visualizes the happiness score for each country, and you can select a specific country to see its key indicators.")
    if country:
        st.write(f"For **{country}**, the happiness score of **{country_data['Score']:.3f}** is influenced by several factors. Its **GDP per capita** of **{country_data['GDP per capita']:.3f}** contributes to a strong sense of economic well-being. The **social support** score of **{country_data['Social support']:.3f}** indicates a robust social fabric, while a **healthy life expectancy** of **{country_data['Healthy life expectancy']:.3f}** reflects the quality of healthcare. The freedom to make life choices, generosity, and perceptions of corruption also play a significant role in the overall happiness of its citizens.")

if __name__ == "__main__":
    main()