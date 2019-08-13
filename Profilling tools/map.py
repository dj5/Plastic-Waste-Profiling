import folium
import pandas as pd
def map():
 PU_COORDINATES= (18.45,73.85)
 df = pd.read_csv("maggi.csv")
 df2= pd.read_csv("pepsi.csv")
 df3= pd.read_csv("cadbury.csv")

 locationsm=[loc[0:-4].split(" ") for loc in df['Name']]
 locationsp=[loc[0:-4].split(" ") for loc in df2['Name']]
 locationsc=[loc[0:-4].split(" ") for loc in df3['Name']]


 popup = folium.Html('<a href="/home/dj/Work/DeepBlue/retina/pie.html">maggi</a>',script=True)
 map = folium.Map(location=PU_COORDINATES, zoom_start=15)

 for each in locationsm:
    map.add_child(folium.CircleMarker(location=[float(each[0]),float(each[1])], popup= folium.Popup(popup),fill=True , fill_color="yellow",    fill_opacity=0.8))
 popup = folium.Html('<a href="/home/dj/Work/DeepBlue/retina/pie.html">pepsi</a>',script=True)
 for each in locationsp:
    map.add_child(folium.CircleMarker(location=[float(each[0])+0.001,float(each[1])], popup= folium.Popup(popup),fill=True , fill_color="blue", fill_opacity=0.8))
 popup = folium.Html('<a href="/home/dj/Work/DeepBlue/retina/pie.html">cadbury</a>',script=True)
 for each in locationsc:
    map.add_child(folium.CircleMarker(location=[float(each[0])+0.001,float(each[1])+0.001], popup= folium.Popup(popup),fill=True , fill_color="brown", fill_opacity=0.8))
 map.save("map.html")
