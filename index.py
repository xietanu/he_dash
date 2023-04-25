"""This is the main file for the app. It contains the layout and the callbacks."""

import dash  # pylint: disable=import-error
import elements
import interfaces

app = dash.Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

server = app.server

app.title = "Higher Education in the UK"

app.layout = dash.html.Div(
    [
        elements.sidebar(
            [
                interfaces.Link(page["name"], page["relative_path"])
                for page in dash.page_registry.values()
            ]
        ),
        dash.page_container,
    ],
    className="basecontainer",
)
