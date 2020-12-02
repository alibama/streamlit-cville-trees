from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import fiona
#from urllib2 import urlopen
#from zipfile import ZipFile
#from StringIO import StringIO
#import shapefile
import geopandas as gpd
#from shapely.geometry import shape  
import datetime
import json, requests, re
"""
# Yet Another Cville Tree App!

Pulling data from http://equity-atlas-uvalibrary.opendata.arcgis.com/

and working on getting opendata.charlottesville.org working as well over here,
https://share.streamlit.io/alibama/cville-trees/main but that's broken... maybe you want to help fix it?  email me at anson@virginia.edu or just fork the repo and send a link...


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


