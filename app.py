from flask import Flask
from views.data import Data
from views.sort import Sort
from views.update import Update
from views.search import Search
from views.map import Map
app = Flask(__name__)


app.register_blueprint(Data)
app.register_blueprint(Sort)
app.register_blueprint(Update)
app.register_blueprint(Search)
app.register_blueprint(Map)

if __name__ == '__main__':
    app.run()
