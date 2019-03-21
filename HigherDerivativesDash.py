import dash
from dash.dependencies import Output, State, Input
import dash_core_components as dcc
import dash_html_components as html

from HigherDerivatives import HigherDerivatives, t, x,\
    x_diff, x_double_diff, x_triple_diff

# ToDo * is bad
from sympy.functions import *
from sympy import pi


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Markdown('''# The Higher Derivatives Problem'''),

    html.Div([html.Label('Enter n'),
              dcc.Input(id='n',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter L'),
              dcc.Input(id='L',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter t0'),
              dcc.Input(id='t0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter t1'),
              dcc.Input(id='t1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x0'),
              dcc.Input(id='x0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x1'),
              dcc.Input(id='x1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    # ToDo Нужен выпадающий список
    html.Div([html.Label('Enter x0_array if necessary'),
              dcc.Input(id='x0_array',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    # ToDo Нужен выпадающий список
    html.Div([html.Label('Enter x1_array if necessary'),
              dcc.Input(id='x1_array',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div(id='my_input')])


@app.callback(Output('my_input', 'children'),
              [Input('n', 'value'),
               Input('L', 'value'),
               Input('t0', 'value'),
               Input('t1', 'value'),
               Input('x0', 'value'),
               Input('x1', 'value'),
               Input('x0_array', 'value'),
               Input('x1_array', 'value')])
def update_output(n, L, t0, t1, x0, x1, x0_array, x1_array):
    if (n is not None) & \
            (L is not None) & \
            (t0 is not None) & \
            (t1 is not None) & \
            (x0 is not None) & \
            (x1 is not None):

        solver = HigherDerivatives(n=eval(n),
                                   L=eval(L),
                                   t0=eval(t0),
                                   t1=eval(t1),
                                   x0=eval(x0),
                                   x1=eval(x1),
                                   x0_array=eval(x0_array),
                                   x1_array=eval(x1_array))
        try:
            solver.solve()
        except:
            to_return = 'Something went wrong :('
        else:
            to_return = html.Div([ dcc.Markdown('### ANSWER'),
                                   dcc.Markdown(f'General solution: {solver.general_solution}'),
                                   dcc.Markdown(f'Coefficients: {solver.coefficients}'),
                                   dcc.Markdown(f'Particular solution: {solver.particular_solution}'),
                                   dcc.Markdown(f'Extreme value: {solver.extreme_value}')],
                                 style={'columnCount': 3})

        return to_return


if __name__ == '__main__':
    app.run_server(port=8060)
