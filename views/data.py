import flask
import json
from models import interface

Data = flask.Blueprint("Data", __name__)


@Data.route('/api/data', methods=['GET'])
def data():
    try:
        info = interface.DataGet()
        response = flask.make_response(info, 200)
        return response
    except Exception as e:
        print(e)
        return 500
