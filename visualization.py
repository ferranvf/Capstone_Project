import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import mysql.connector
import numpy as np
from obtain_data import *
import sys



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
    df = get_data(col_chosen, cnx)
    degree_type = df['degree_type'].values[0]
    df = create_data(df, cnx)

    if degree_type == 'BS' or degree_type == 'BA':
        path = ['degree', 'year_taken','semester_taken','restriction_description' ,'course_name']
    else:
        path = ['degree','course_type', 'parent_description', 'restriction_description','course_name']
    
    fig = px.icicle(df, path=path)
    fig.update_traces(root_color='lightgrey')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.write_html("htmlfiles/"+col_chosen + "_visualization_1.html")
    return fig

def visualization_2(degree,cnx):
    df = get_data(degree, cnx)
    df = create_data2(df, cnx)
    fig = px.sunburst(df, path=['degree', 'course_name', 'longdescription'])
    # set title
    fig.update_layout(title={
        'text': 'Learning Obejectives',
        'x': 0.5, # sets the x-axis position to the center
        'y': 0.95 # sets the y-axis position to be just above the chart
    })
    # show chart
    fig.write_html("htmlfiles/"+degree + "_visualization_2.html")
    fig.show()

def connect_database():
    cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')
    
    return cnx

    
if __name__ == '__main__':
    cnx = connect_database()
    
    rerun = 1
    while rerun == 1:
        choice = int(input("Select which data visualization do you want to see: \n 1: Program courses. \n 2: Learning Objectives \n Your choice: "))
        if choice == 1:
            visualization_1(cnx)
            app.run_server(debug=False)
        elif choice == 2:
            visualization_2("Computational Data Science", cnx)
        else:
            print("Wrong choice")
        rerun = int(input("Do you want to visualize anything else? \n 1: Yes \n 2: No \n Your choice: "))
    