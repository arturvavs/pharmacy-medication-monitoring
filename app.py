import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from warnings import filterwarnings

filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')
filterwarnings("ignore", category=FutureWarning, message='.*deprecated and will be removed in a future version. To read from a literal string*')
#FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
app = Dash(__name__,pages_folder='pages', use_pages=True, suppress_callback_exceptions=True, external_stylesheets=['assets/styles.css'], assets_folder='assets')




if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port='8051',debug=True, dev_tools_ui=False)