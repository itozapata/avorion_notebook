import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = dbc.Navbar([
    html.A(
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url("logo.png"), height="60px",style={'stroke':'#508caf'})),
            dbc.Col(dbc.NavbarBrand("Space Idiots", className="ml-2",
                                    style={'fontSize':'2em', 'fontWeight':'900', 'color':'#508caf'})),
        ],align="center",no_gutters=True),
    href='#'),

    dbc.NavbarToggler(id="navbar-toggler",className="ml-auto"),

    dbc.Collapse(
        dbc.Row([
            dbc.NavLink("MAP", href='#'),
            dbc.NavLink("TIMELINE", href='#timeline', external_link=True),
            dbc.NavLink("PROGRESSION", href='#progression', external_link=True),
            dbc.NavLink("ABOUT", href='#about', external_link=True),
        ],no_gutters=True, className="ml-auto flex-nowrap mt-3 mt-md-0",align="center"),
        id="navbar-collapse", navbar=True),

],sticky="top",className='mb-4 bg-white',style={'WebkitBoxShadow': '0px 5px 5px 0px rgba(100, 100, 100, 0.1)',})
