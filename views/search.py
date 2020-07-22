import flask
import json
from models import interface

Search = flask.Blueprint("Search", __name__)


@Search.route('/api/search/list', methods=['GET'])
def search_list():
    try:
        list_search = [{"id": 1, "name": "暴力搜索"}]
        response = flask.make_response(json.dumps(list_search), 200)
        return response
    except Exception as e:
        print(e)
        return 500


@Search.route('/api/search/<int:id>', methods=['POST'])
def sort_id(id):
    try:
        post_data = json.loads(flask.request.get_data(as_text=True))
        data = post_data['data']
        if id == 1:
            info = interface.DataSearch(data)
            print(info)
            response = flask.make_response(info, 200)
            return response
        else:
            return flask.make_response({"message": "方法错误"}, 200)
    except Exception as e:
        print(e)
        return 500
