import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table, Input, Output

# Load and prepare data
df = pd.read_csv("C:/Users/Muneeb Mughal/Desktop/dashboaRD/financial_Accounting.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%b")
df["Amount"] = df["Credit"].fillna(0) - df["Debit"].fillna(0)

# Initial values
earliest_date = df["Date"].min()
latest_date = df["Date"].max()

# App
app = Dash(__name__)
app.title = "📊 Financial Dashboard"

app.layout = html.Div(style={"backgroundColor": "#000", "padding": "20px", "fontFamily": "Arial"}, children=[
    html.H1("📈 Financial Dashboard", style={"textAlign": "center", "color": "#FFD700"}),

    # Date range filter
    html.Div([
        html.Label("Select Date Range:", style={"color": "#FFD700"}),
        dcc.DatePickerRange(
            id="date-range",
            min_date_allowed=earliest_date,
            max_date_allowed=latest_date,
            start_date=earliest_date,
            end_date=latest_date,
            display_format="YYYY-MM-DD",
            style={"color": "#000"}
        )
    ], style={"marginBottom": "20px"}),

    # KPIs
    html.Div(id="kpi-cards", style={"display": "flex", "justifyContent": "space-between", "marginBottom": "20px"}),

    # Charts
    html.Div([
        dcc.Graph(id="monthly-bar"),
        dcc.Graph(id="line-chart"),
        dcc.Graph(id="donut-chart")
    ]),

    # Table
    html.Div([
        html.H3("🏆 Top 10 Transactions", style={"textAlign": "center", "color": "#FFD700"}),
        dash_table.DataTable(
            id="top-table",
            style_table={"overflowX": "auto"},
            style_cell={"backgroundColor": "#111", "color": "#FFD700", "textAlign": "left"},
            style_header={"backgroundColor": "#222", "fontWeight": "bold", "color": "#FFD700"},
        )
    ])
])

@app.callback(
    [Output("kpi-cards", "children"),
     Output("monthly-bar", "figure"),
     Output("line-chart", "figure"),
     Output("donut-chart", "figure"),
     Output("top-table", "data"),
     Output("top-table", "columns")],
    [Input("date-range", "start_date"),
     Input("date-range", "end_date")]
)
def update_dashboard(start_date, end_date):
    # Filter data
    dff = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # KPIs
    total_income = dff[dff["Transaction_Type"] == "Income"]["Credit"].sum()
    total_expense = dff[dff["Transaction_Type"] == "Expense"]["Debit"].sum()
    balance = total_income - total_expense

    kpis = [
        html.Div([
            html.Div("Total Income", style={"color": "#000"}),
            html.H3(f"${total_income:,.2f}", style={"color": "#000"})
        ], style={"backgroundColor": "#FFD700", "padding": "15px", "borderRadius": "10px", "width": "32%"}),

        html.Div([
            html.Div("Total Expense", style={"color": "#000"}),
            html.H3(f"${total_expense:,.2f}", style={"color": "#000"})
        ], style={"backgroundColor": "#FFD700", "padding": "15px", "borderRadius": "10px", "width": "32%"}),

        html.Div([
            html.Div("Balance", style={"color": "#000"}),
            html.H3(f"${balance:,.2f}", style={"color": "#000"})
        ], style={"backgroundColor": "#FFD700", "padding": "15px", "borderRadius": "10px", "width": "32%"})
    ]

    # Charts
    monthly = dff.groupby(["Month", "Transaction_Type"]).agg({"Credit": "sum", "Debit": "sum"}).reset_index()
    bar_fig = px.bar(monthly, x="Month", y="Credit", color="Transaction_Type", barmode="group",
                     title="Monthly Income vs Expense", template="plotly_dark",
                     color_discrete_map={"Income": "yellow", "Expense": "orange"})

    daily = dff.groupby("Date").sum(numeric_only=True).reset_index()
    line_fig = px.line(daily, x="Date", y=["Credit", "Debit"],
                       title="Income & Expense Over Time", template="plotly_dark")

    category_summary = dff.groupby("Category").agg({"Debit": "sum"}).reset_index()
    donut_fig = px.pie(category_summary, names="Category", values="Debit",
                       title="Expense Distribution by Category", hole=0.4,
                       template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Safe)

    # Table
    table_df = dff[["Date", "Payment_Method", "Debit", "Credit", "Description", "Category"]]
    table_df = table_df.sort_values(by=["Credit", "Debit"], ascending=False).head(10)
    columns = [{"name": col, "id": col} for col in table_df.columns]
    data = table_df.to_dict("records")

    return kpis, bar_fig, line_fig, donut_fig, data, columns

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:8051")  # Automatically open browser
    app.run(debug=False, port=8051)