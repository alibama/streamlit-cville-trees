from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import fiona
import geopandas as gpd
import requests
import datetime
import json, re


"""
# Welcome to The Cville Tree Commission Neighborhood Tree App!

Editing `/streamlit_app.py` customizes this app
aloha
"""


"""
I'm using just pandas to read in the CSV from the equity map project at UVa
this is a stupid way to do things with CSV files going through pandas... pulling the data in as CSV and the renaming the columns... 
however it works and before i found out that geopandas would take files directly in here it was approach #1

"""

df=gpd.read_csv("https://opendata.arcgis.com/datasets/e7c856379492408e9543a25d684b8311_79.csv")

trees=df.rename(columns={"X": "lon", "Y": "lat"})
st.map(trees)
data_top = trees.head()
data_top  

"""
https://gis.stackexchange.com/questions/225586/reading-raw-data-into-geopandas and then i read this fine manual and it's really simple to import shape files straight from zip in to geopandas
"""

zip_url = 'http://widget.charlottesville.org/gis/zip_download/planning_area.zip'
cvillehoods = gpd.read_file(zip_url)


trees_in_hoods=gpd.sjoin(trees, cvillehoods, how="inner", op='intersects')

test=trees_in_hoods.head()
test
#st.map(cvillehoods)


      






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
