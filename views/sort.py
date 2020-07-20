import flask
import json
from models import interface

Sort = flask.Blueprint("Sort", __name__)


@Sort.route('/api/sort/list', methods=['GET'])
def sort_list():
    try:
        info = interface.SortMethodGet()
        response = flask.make_response(info, 200)
        return response
    except Exception as e:
        print(e)
        return 500


@Sort.route('/api/sort/<int:id>', methods=['GET'])
def sort_id(id):
    try:
        # interface.init_r()
        time = interface.ExecSort(id)
        result = interface.DataGet()
        info = {'time': time, 'result': result}
        response = flask.make_response(json.dumps(info), 200)
        return response
    except Exception as e:
        print(e)
        return 500
