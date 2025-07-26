# financial_dashboard.py
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import os

# Load or create data
file_path = os.path.expanduser("~/Desktop/financial_Accounting.csv")
if not os.path.exists(file_path):
    data = {
        "Date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
        "Category": ["Groceries", "Utilities", "Rent", "Transport", "Entertainment"] * 20,
        "Credit": [500, 0, 0, 0, 0] * 20,
        "Debit": [0, 150, 1000, 100, 200] * 20,
        "Payment_Method": ["Cash", "Bank", "Card", "Online", "Check"] * 20
    }
    pd.DataFrame(data).to_csv(file_path, index=False)

df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"])

# KPIs
total_credit = df["Credit"].sum()
total_debit = df["Debit"].sum()
net_balance = total_credit - total_debit

# Create Dash app
app = Dash(__name__)
app.title = "💰 Financial Dashboard"

app.layout = html.Div(style={
    "backgroundColor": "#000",
    "color": "#FFD700",
    "fontFamily": "Arial",
    "padding": "20px"
}, children=[
    html.H1("📊 Financial Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.H4("Total Credit"),
            html.H2(f"${total_credit:,.2f}")
        ], style={"backgroundColor": "#222", "padding": "15px", "borderRadius": "10px", "width": "30%"}),

        html.Div([
            html.H4("Total Debit"),
            html.H2(f"${total_debit:,.2f}")
        ], style={"backgroundColor": "#222", "padding": "15px", "borderRadius": "10px", "width": "30%"}),

        html.Div([
            html.H4("Net Balance"),
            html.H2(f"${net_balance:,.2f}")
        ], style={"backgroundColor": "#222", "padding": "15px", "borderRadius": "10px", "width": "30%"})
    ], style={"display": "flex", "justifyContent": "space-around", "marginBottom": "30px"}),

    dcc.Graph(figure=px.bar(df, x="Category", y="Debit", color="Category",
                            title="Debit by Category", template="plotly_dark",
                            color_discrete_sequence=["#FFD700"])),
    
    dcc.Graph(figure=px.line(df.groupby("Date")["Credit"].sum().reset_index(),
                             x="Date", y="Credit", title="Credit Over Time",
                             template="plotly_dark", markers=True, line_shape="spline",
                             color_discrete_sequence=["#FFD700"])),

    dcc.Graph(figure=px.pie(df, names="Payment_Method", values="Debit",
                            title="Payment Methods Share", template="plotly_dark",
                            color_discrete_sequence=px.colors.sequential.YlOrBr)),

    dcc.Graph(figure=px.density_heatmap(df, x="Category", y="Payment_Method", z="Debit",
                                        title="Heatmap of Debit by Category and Payment Method",
                                        template="plotly_dark", color_continuous_scale="YlOrBr")),
])

if __name__ == "__main__":
    app.run_server(debug=False)
