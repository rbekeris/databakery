from flask import render_template
from . import main
import plotly
import plotly.graph_objs as go
import json

def create_plot():
    trace_1 = go.Scatter(
                        x=(1,2,3),
                        y=(1,2,3),
                        mode='lines+markers',
                        name ='Player_1')
    trace_2 = go.Scatter(
                        x=(1,2,3),
                        y=(2,3,4),
                        mode='lines+markers',
                        name = 'Player_2')                 
    data = [trace_1, trace_2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@main.route('/')

def index():
    bar = create_plot()
    return render_template('index.html', plot = bar)
