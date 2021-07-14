from selenium import webdriver
import folium

s_map = folium.Map(location=[37.55,126.98],zoom_start=12);
s_map.save('./s_map.html');