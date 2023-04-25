"""Create the sidebar navigation."""
import dash # pylint: disable=import-error
import interfaces


def sidebar(links: list[interfaces.Link]) -> dash.html.Nav:
    """Create the sidebar navigation."""
    return dash.html.Nav(
        [
            dash.html.H1("UKHE"),
            dash.html.P("UK Higher Education Dashboard"),
            dash.html.Hr(),
            dash.html.Ul(
                [dash.html.Li(dash.html.A(link.text, href=link.url)) for link in links]
            ),
        ],
        className="sidebar",
    )
