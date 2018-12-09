from dash_dagre import DagreD3
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div(id='svg_container', children=[
    DagreD3(
        id="dag",
        nodes={
                    '1': {
                        'label': 'Node 1',
                        'rx': 10,
                        'ry': 10,
                    },
                    '2': {
                        'label': 'Node 2',
                        'rx': 5,
                        'ry': 5,
                    },
                    '3': {
                        'label': 'Node 3',
                        'rx': 5,
                        'ry': 5,
                    },
                    '4': {
                        'label': 'Node 4',
                        'rx': 5,
                        'ry': 5,
                    },
                    '5': {
                        'label': 'Node 5',
                        'rx': 5,
                        'ry': 5,
                    },
                    '6': {
                        'label': 'Node 6',
                        'rx': 5,
                        'ry': 5,
                    }
                }
        ,
        edges=[
                    ['1', '2', {}],
                    ['1', '3', {}],
                    ['2', '4', {}],
                    ['2', '3', {}],
                    ['1', '4', {}],
                    ['5', '4', {}],
                    ['6', '4', {}],
                    ['3', '4', {}]
        ],
        width=''
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('dag', 'selectedId')]
)
def show_task_info(selectedId):
    if selectedId is not None:
        return "You have selected node #{}".format(selectedId)

if __name__ == '__main__':
    app.run_server(debug=True)