import flask
import json

Data = flask.Blueprint("Data", __name__)


@Data.route('/api/data', methods=['GET'])
def data():
    try:
        info = {"name": "hello"}
        response = flask.make_response(json.dumps(info), 200)
        return response
    except Exception as e:
        print(e)
        return 500
