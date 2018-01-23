from flask import Flask, request
import flask
import yaml


app = Flask(__name__)

@app.route('/api')
def my_microservice():
    resp = flask.Response(yaml.safe_dump(['Hello', 'YAML', 'World!']))
    if request.headers is not None:
        resp.headers['Content-Type'] = 'application/x-yaml'
    return resp

if __name__ == '__main__':
    app.run()
