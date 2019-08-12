import dash_core_components as dcc
import dash_html_components as html
from components import Header, print_button,pydf
import dash_bootstrap_components as dbc
import pymongo
import pandas as pd
import dash_table as dt
from data import df


######################## mongo db data ########################
# use this to import csv into local mongo db
# mongoimport --db db_dash --collection collection_dash --type csv 
# --headerline --file data/data.csv

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_dash"]
mycol = mydb["collection_dash"]

df1 = pd.DataFrame(list(mycol.find()))
df=((df1[['Date','Travel Product']]))
######################## START HOME Layout ########################


layout1 = html.Div([
    html.Div([
        # CC Header
        Header(),
    html.H3('HOME'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),


    dcc.Link('Go to App 2', href='/apps/app2'),
    html.Div([
    html.A(html.Button('Download Data', id='download-button'), id='download-link-birst-category'),
    html.A(html.Button('Upload Data', id='upload-button'), id='upload-link-birst-category')
    
        ]),
    ])
])

######################## START EMPLOYEES Layout ########################


layout2 = html.Div([
    html.Div([
        # CC Header
        Header(),
    html.H3('EMPLOYESS'),
    html.Div([
        dbc.Row(dbc.Col(
            # dash table
            dt.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=(df.head()).to_dict('records'),
                editable=True,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                row_selectable="multi",
                selected_rows=[],
                fixed_rows={'headers': True, 'data': 0},
                style_table={'overflowX': 'scroll',
                             'textAlign': 'left',
                             },
            ),
        )),

    ]),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Div([
    html.A(html.Button('Download Data', id='downlad-button'), id='download-link-birst-category'),
    html.A(html.Button('Upload Data', id='upload-button'), id='upload-link-birst-category')
    
        ]),
    ])
])

######################## START REPAYMENTS Layout ########################


layout3 = html.Div([
    html.Div([
        # CC Header
        Header(),
    html.H3('REPAYMENTS'),
    dcc.Dropdown(
        id='app-3-dropdown',
        options=[
            {'label': 'App 3 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-3-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Div([
    html.A(html.Button('Download Data', id='download-button'), id='download-link-birst-category'),
    html.A(html.Button('Upload Data', id='upload-button'), id='upload-link-birst-category')
    
        ]),
    ])
])