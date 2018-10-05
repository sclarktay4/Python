import geopy
import folium
import os, webbrowser

from geopy.geocoders import Nominatim

from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('encodings')

#Create the nom object for project      
nom = Nominatim(user_agent = "Script")
#user's entered location
data =input('Enter the address: ')
#stored user entered location
here = nom.geocode(data)
#get latitude
Latt = here.latitude
#get longitude
Lon = here.longitude
#output user entered location, Latitude, and Longitude
print(here)
print(Latt, Lon)
#create map opject
map = folium.Map([Latt, Lon],zoom_start=10, tiles='Stamen Terrain')
#create marker on map for entered location
folium.Marker(location=[Latt, Lon], popup=data).add_to(map)
#save data to html file
map.save("wb_test.html")
#open map in browser
webbrowser.open("wb_test.html")
