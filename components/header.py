import dash_html_components as html
import dash_core_components as dcc


def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://i.imgur.com/KAz2xrq.jpg', height='101', width='141')
        ], className="twenty columns padded"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo



def get_header():
    header = html.Div([

        html.Div([
            html.H1(
                'KARMA LIFE')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header

def get_menu():
    menu = html.Div([

        dcc.Link('HOME    ', href='/apps/app1', className="tab first"),
        html.Br([]),

        dcc.Link('EMPLOYEES   ', href='/apps/app2', className="tab"),
        html.Br([]),

        dcc.Link('REPAYMENTS   ', href='/apps/app3', className="tab"),
        html.Br([]),

        dcc.Link('REPORT   ', href='/apps/app3', className="tab"),
        html.Br([])

       
    ], className="row ")
    return menu


