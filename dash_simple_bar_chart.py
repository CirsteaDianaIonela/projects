import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas_practice as pd

external_stylesheets = ['http://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#instantiem app mai sus
cars_data = pd.DataFrame({
    "Company": ["Tesla", "Tesla", "Tesla", "Ford", "Ford", "Ford"],
    "State": ["California", "Washington", "Oregon", "California", "Washington", "Oregon"],
    "Sales": [6, 3, 6, 4, 8, 10]
})
fig = px.bar(cars_data,
             x="Company",
             y="Sales",
             color="State",
             barmode="group")

fig.update_layout(
    title_text='Sale of Tesla and Ford',
    plot_bgcolor='ivory',
    paper_bgcolor='linen',
    font_color='darkslategray',
    font_family='Arial',
    font_size=20,
    legend_font_family='Georgia',
    legend_font_size=15

)

app.layout = html.Div(children=[
    html.H2(children='Car Sales in CA, OR and WA'),
    dcc.Graph(
        id='sample-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    