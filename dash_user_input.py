import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['http://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Change the value in the text box."),
    html.Br(),
    html.Div(["Text:", dcc.Input(id='input', type='text')]),
    html.Br(),
    html.Div(id='output'),
], style={'padding': 50})

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    return 'Return Value: {}'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)