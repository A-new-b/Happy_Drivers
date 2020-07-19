from flask import Flask

from .views.data import Data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(Data)

if __name__ == '__main__':
    app.run()
