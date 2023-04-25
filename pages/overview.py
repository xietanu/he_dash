"""Overview page."""
import dash  # pylint: disable=import-error

dash.register_page(__name__, path="/")

layout = dash.html.Div([dash.html.H2("Overview"), "Testing"], className="content")
