from flask import Flask
from views.data import Data
from views.sort import Sort
from views.update import Update
import json

app = Flask(__name__)


app.register_blueprint(Data)
app.register_blueprint(Sort)
app.register_blueprint(Update)


if __name__ == '__main__':
    app.run()
