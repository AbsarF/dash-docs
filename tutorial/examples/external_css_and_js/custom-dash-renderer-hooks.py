import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>Testing custom DashRenderer</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            <script id="_dash-renderer" type"application/json">
                const renderer = new DashRenderer({
                    request_pre: (payload) => {
                        // print out payload parameter
                        console.log(payload);
                    },
                    request_post: (payload, response) => {
                        // print out payload and response parameter
                        console.log(payload);
                        console.log(response);
                    }
                })
            </script>
        </footer>
        <div>With request hooks</div>
    </body>
</html>
'''

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)
