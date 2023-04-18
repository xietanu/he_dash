"""This is the main file for the app. It contains the layout and the callbacks."""

import dash  # pylint: disable=import-error

app = dash.Dash(__name__, suppress_callback_exceptions=True)

server = app.server

app.title = "Higher Education in the UK"

app.layout = dash.html.Div(
    [
        dash.html.P(
            "Higher Education in the UK",
        ),
    ]
)
