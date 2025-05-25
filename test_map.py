import streamlit as st
import folium
from streamlit_folium import folium_static

st.title("Map Test")

# Einfache Test-Karte
m = folium.Map(location=[53.5511, 9.9937], zoom_start=10)
folium.Marker([53.5511, 9.9937], popup="Hamburg").add_to(m)

folium_static(m)