from flask import Flask
from views.data import Data
from views.sort import Sort
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = {"name": "Hello"}
    return json.dumps(a)


app.register_blueprint(Data)
app.register_blueprint(Sort)


if __name__ == '__main__':
    app.run()
