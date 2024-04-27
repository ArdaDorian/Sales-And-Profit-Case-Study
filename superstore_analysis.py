import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#region funcs
def createLineFig(_data, _x, _y, _title):
    fig= px.line(_data, x=_x, y=_y, title=_title)
    return fig

def createPieFig(_data, _values, _names, _title):
    fig= px.pie(_data, values=_values, names=_names, color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(title_text = _title)
    fig.update_traces(textposition= "inside", textinfo="label+percent")
    return fig

def createBarFig(_data, _x, _y, _title):
    fig = px.bar(_data, x=_x, y=_y, title=_title)
    return fig

def createMultiBarFig(_data, _x, _y, _title, _count):
    fig=go.Figure()
    for i in range(_count):
        fig.add_trace(go.Bar(x=_data[_x], y=_data[_y[i]], name=_y[i], marker_color=px.colors.qualitative.Pastel[i]))
    fig.update_layout(title=_title, xaxis_title= _x, yaxis_title="Amount")
    return fig


#regionend funcs

df = pd.read_csv("SuperStoreSample.csv", encoding="latin-1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Order Date"])

df["Order Month"] = df["Order Date"].dt.month

# Seasonality of sales
sales_by_months = df.groupby("Order Month")["Sales"].sum().reset_index()
fig_sbm = createLineFig(sales_by_months, "Order Month", "Sales", "Sales by Months")
fig_sbm.show()

# Ratio of categories
sales_by_categories = df.groupby("Category")["Sales"].sum().reset_index()
fig_sbc = createPieFig(sales_by_categories, "Sales", "Category", "Sales by Categories")
fig_sbc.show()

# Sales of subcategories
sales_by_subcategories = df.groupby("Sub-Category")["Sales"].sum().reset_index()
fig_sbs = createBarFig(sales_by_subcategories, "Sub-Category", "Sales", "Sub-Category Sale Numbers")
fig_sbs.show()

# Monthly Profit
profit_by_months = df.groupby("Order Month")["Profit"].sum().reset_index()
fig_pbm = createLineFig(profit_by_months, "Order Month", "Profit", "Profits by Months")
fig_pbm.show()

# Profit for categories
profit_by_categories = df.groupby("Category")["Profit"].sum().reset_index()
fig_pbc = createPieFig(profit_by_categories, "Profit", "Category", "Profits by Categories")
fig_pbc.show()

# Profit for subcategories
profit_by_subcategories = df.groupby("Sub-Category")["Profit"].sum().reset_index()
fig_pbs = createBarFig(profit_by_subcategories, "Sub-Category", "Profit", "Profits by Subcategories")
fig_pbs.show()

# Sales & Profits for segments
sales_profit_by_segments = df.groupby("Segment").agg({"Sales": "sum", "Profit": "sum"}).reset_index()
fig_spbs = createMultiBarFig(sales_profit_by_segments, "Segment", ["Sales", "Profit"], "Sales and Profit Amount by Segments", 2)
fig_spbs.show()