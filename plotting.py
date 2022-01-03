from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

# creates graph figure object
p = figure(x_axis_type='datetime', height=100, width=500, title='Motion Detector Graph')

# modifying tick color on graph
p.yaxis.minor_tick_line_color = None

# Adds hover tool from bokeh library for messages when hovering over objects in the graph
hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End ", "@End_string")])
p.add_tools(hover)

# Modifying graph -- Objet displays on the graph
q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

# Output and show file
output_file("Graph1.html")
show(p)
