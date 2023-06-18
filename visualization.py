import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import mysql.connector
import numpy as np
from obtain_data import *



app = Dash(__name__)

def visualization_1(cnx):
    q = ("select degree_name from Degrees")
    degrees =  pd.read_sql(q, cnx)
    degrees = list(degrees['degree_name'].unique())
    
    app.layout = html.Div([
        html.Div(children='Temple University')
    ,
    dcc.Dropdown(degrees,"Computational Data Science",id='drop-down-degrees'),
    dcc.Graph(figure={}, id='controls-and-graph')])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='drop-down-degrees', component_property='value')
)

def update_data(col_chosen):
    print(col_chosen)
    df = get_data(col_chosen, cnx)
    degree_type = df['degree_type'].values[0]
    df = create_data(df, cnx)

    if degree_type == 'BS' or degree_type == 'BA':
        path = ['degree', 'year_taken','semester_taken','restriction_id' ,'course_name']
    else:
        path = ['degree','course_type', 'parent_id', 'restriction_id','course_name']
    
    fig = px.icicle(df, path=path)
    fig.update_traces(root_color='lightgrey')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    return fig

def connect_database():
    cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')
    
    return cnx

    
if __name__ == '__main__':
    cnx = connect_database()
    visualization_1(cnx)
    app.run_server(debug=True)
