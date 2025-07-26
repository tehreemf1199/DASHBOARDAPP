import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("financial_Accounting.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Dash app
app = Dash(__name__)
app.title = "📊 Financial Dashboard"

# Layout
app.layout = html.Div([
    html.Div([
        html.H2("📈 Financial Dashboard", style={"marginBottom": "10px"}),
        dcc.RadioItems(
            id="theme-toggle",
            options=[
                {"label": "🌞 Light", "value": "light"},
                {"label": "🌙 Dark", "value": "dark"},
            ],
            value="dark",
            labelStyle={"display": "inline-block", "marginRight": "10px"},
            style={"textAlign": "right"}
        )
    ], style={
        "display": "flex",
        "flexDirection": "column",
        "gap": "10px",
        "padding": "10px"
    }),

    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="line-chart"),
], id="main-container")

# Callback
@app.callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Output("main-container", "className"),
    Input("theme-toggle", "value")
)
def update_dashboard(theme):
    bar_fig = px.bar(df, x="Category", y="Credit", color="Category", title="Credit by Category")
    line_fig = px.line(df.groupby("Date")["Credit"].sum().reset_index(), x="Date", y="Credit", title="Credit Over Time")

    if theme == "dark":
        bar_fig.update_layout(template="plotly_dark")
        line_fig.update_layout(template="plotly_dark")
        return bar_fig, line_fig, "dark-mode"
    else:
        bar_fig.update_layout(template="plotly_white")
        line_fig.update_layout(template="plotly_white")
        return bar_fig, line_fig, "light-mode"

# Expose server for desktop launcher
server = app.server
