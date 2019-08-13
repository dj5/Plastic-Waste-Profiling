from math import pi

import pandas as pd
from bokeh.layouts import gridplot,row
from bokeh.io import output_file, save
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap
def chart():
 output_file("pie.html")
 df = pd.read_csv("maggi.csv")
 df2= pd.read_csv("pepsi.csv")
 df3= pd.read_csv("cadbury.csv")
 
 locationsm=[loc[0:-4].split(" ") for loc in df['Name']]
 locationsp=[loc[0:-4].split(" ") for loc in df2['Name']]
 locationsc=[loc[0:-4].split(" ") for loc in df3['Name']]
 countc=len(locationsc)

 countm=len(locationsm)
 countp=len(locationsp)

 x = {
'maggi':countm,
'pepsi':countp,
'cadbury':countc
 
 }

 data = pd.Series(x).reset_index(name='value').rename(columns={'index':'pwp'})
 pwp=data['pwp']
 value=data['value']
 print(data)
 data['angle'] = data['value']/data['value'].sum() * 2*pi
 data['color'] =  Category20c[len(x)]#['yellow','blue']
 
 p = figure(plot_height=450, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@pwp: @value", x_range=(-0.5, 1.0))

 p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='pwp', source=data)
 p.axis.axis_label=None
 p.axis.visible=False
 p.grid.grid_line_color = None
 print(data)
 
 p2 = figure(x_range=pwp, plot_height=450, tools="hover" , title="PWP")
 p2.vbar(x=pwp, top=value, width=0.9)

 grid = row(p,p2) 
 #grid = gridplot([p, p2], ncols=2, plot_width=350, plot_height=350)

 save(grid)
