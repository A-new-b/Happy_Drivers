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


@Sort.route('/api/sort/<int:id>', methods=['POST'])
def sort_id(id):
    try:
        time = interface.ExecSort(id)
        post_data = json.loads(flask.request.get_data(as_text=True))
        start = post_data['start']
        end = post_data['end']
        nums = interface.GetRecordCount_i()
        info = {'time': time, 'nums': nums, 'info': interface.DataGetEx(start, end)}
        response = flask.make_response(json.dumps(info), 200)
        return response
    except Exception as e:
        print(e)
        return 500
