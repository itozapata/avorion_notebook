import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    dbc.themes.BOOTSTRAP,
    'https://use.fontawesome.com/releases/v5.11.2/css/all.css',
    {'href':'https://fonts.googleapis.com/icon?family=Material+Icons', 'rel':'stylesheet'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
