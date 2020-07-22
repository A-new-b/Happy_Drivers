import flask
import json
from models import interface
import os

fileManage = flask.Blueprint("fileManage", __name__)


@fileManage.route('/api/img', methods=["Get"])
def getImg():
    try:
        imgUrl = flask.request.args.get("imgUrl")
        file_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'img', imgUrl)

        if os.path.exists(file_path):
            return flask.send_file(file_path, "temp.jpg", as_attachment=True)
        else:
            return {"message": "路径错误"}, 404
    except Exception as e:
        print(e)
        return {"message": "服务器错误"}, 500
