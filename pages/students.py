"""Students page."""
import dash  # pylint: disable=import-error

dash.register_page(__name__)

layout = dash.html.Div([dash.html.H2("Students"), "Test"], className="content")
