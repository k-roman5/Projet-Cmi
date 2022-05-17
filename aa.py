SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "width": "90rem",
    "padding": "2rem 1rem",
    "text-align": "center",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
image_file_name = "simple-oak-tree-logo-design-260nw-1759587047.jpg"
encoded_image = base64.b64encode(open(image_file_name, "rb").read())

sidebar = html.Div(
    [dbc.NavLink(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())), href="/",
                 active="exact"),
        html.H2("CMI ISI", className="display-4",),
        html.P(
            u"Forêt Pyrénnées", className="lead"
    ),
        dbc.Nav(
            [
                dbc.NavLink("Histogramme", href="/histogramme",
                            active="exact"),
                dbc.NavLink("Tableur", href="/table",
                            active="exact"),
            ],
            horizontal=True,
            pills=True,
    ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])
