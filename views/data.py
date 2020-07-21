import flask
import json
from models import interface

Data = flask.Blueprint("Data", __name__)


@Data.route('/api/data', methods=['POST'])
def data():
    try:
        post_data = json.loads(flask.request.get_data(as_text=True))
        start = post_data['start']
        end = post_data['end']
        info = interface.DataGetEx(start, end)
        nums = interface.GetRecordCount_i()
        info = {"info": info, "nums": nums}
        response = flask.make_response(info, 200)
        return response
    except Exception as e:
        print(e)
        return 500
