import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_daq as daq

external_stylesheets = ['http://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.BooleanSwitch(id='boolean-switch', on=True, color="Blue"),
    html.Div(id='boolean-switch-output')
])

@app.callback(
    dash.dependencies.Output('boolean-switch-output', 'children'),
    [dash.dependencies.Input('boolean-switch', 'on')])
def update_output(switch_status):
    return 'The switch is {}.'.format(switch_status)
if __name__ == '__main__':
    app.run_server(debug=True)
