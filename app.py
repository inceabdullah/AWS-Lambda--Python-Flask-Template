from flask import request
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)


@app.route('/foo', methods=['GET', 'POST'])
def foo():
    data = {
        'form': request.form.copy(),
        'args': request.args.copy(),
        'json': request.json
    }
    return (
        """<html><header><title>titttleeee</title></header></html>""",
        200,
        {'Content-Type': 'text/html'}
    )


if __name__ == '__main__':
    app.run(debug=True)