import dash_core_components as dcc
import dash_html_components as html
from components import Header, print_button

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
    html.A(html.Button('Download Data', id='download-button'), id='download-link-birst-category')
        ]),
    ])
])

######################## START EMPLOYEES Layout ########################


layout2 = html.Div([
    html.H3('EMPLOYESS'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])

######################## START REPAYMENTS Layout ########################


layout3 = html.Div([
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
    dcc.Link('Go to App 1', href='/apps/app1')
])