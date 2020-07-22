import flask
import json
import os

Update = flask.Blueprint("Update", __name__)


@Update.route('/api/update', methods=['Post'])
def upload():
    try:
        f = flask.request.files['file']
        basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 当前文件上级目录
        upload_path = os.path.join(basePath, 'models', 'GTBL.dat')
        print(upload_path)
        f.save(upload_path)
        return {"message":"success"}
    except Exception as e:
        print(e)
        return 500
