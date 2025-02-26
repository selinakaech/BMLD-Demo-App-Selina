import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Titel der App
st.title("Geografische Daten auf interaktiven Karten")

# Beispiel-Daten laden
@st.cache_data
def load_data():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    return world

data = load_data()

# Daten anzeigen
st.write("Geografische Daten:")
st.write(data.head())

# Interaktive Karte erstellen
st.write("Interaktive Karte:")
m = folium.Map(location=[20, 0], zoom_start=2)

# Daten auf der Karte darstellen
for _, row in data.iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=row['name']
    ).add_to(m)

# Karte in Streamlit anzeigen
st_folium(m, width=700, height=500)