#!pip install geopandas
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import geopandas as gpd
import datetime
import json, requests, re
"""
# Welcome to The Cville Tree Commission Neighborhood Tree App!
Have a great day
hello
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

"""
#cvilletrees = "https://opendata.arcgis.com/datasets/e7c856379492408e9543a25d684b8311_79.geojson"
#treesdf = gpd.read_file(cvilletrees)   


#url = ("https://opendata.arcgis.com/datasets/e7c856379492408e9543a25d684b8311_79.geojson")
#request = requests.get(url)
#zipfile = "zip::http://widget.charlottesville.org/gis/zip_download/planning_area.zip!planning_area_09_03_2020.shp"
#city_hoods=gpd.read_file(zipfile)
#r = requests.get('https://opendata.arcgis.com/datasets/e7c856379492408e9543a25d684b8311_79.geojson')
#j = r.json()
#df = pd.DataFrame.from_dict(r)

#this is a stupid way to do things... pulling the data in as CSV and the renaming the columns... 
df=pd.read_csv("https://opendata.arcgis.com/datasets/e7c856379492408e9543a25d684b8311_79.csv")

df=df.rename(columns={"X": "lon", "Y": "lat"})
st.map(df)
data_top = df.head()
data_top  

city = gpd.read_file('https://github.com/alibama/streamlit-example/blob/master/planning_area_09_03_2020.shp')

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')
    

    
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [38.76, -78.4],
#    columns=['lat', 'lon'])

#st.map(map_data)
