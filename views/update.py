import flask
import os
from models import interface
Update = flask.Blueprint("Update", __name__)


@Update.route('/api/update', methods=['Post'])
def upload():
    try:
        f = flask.request.files['file']
        basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 当前文件上级目录
        upload_path = os.path.join(basePath, 'models', 'Test.dat')
        f.save(upload_path)
        result = interface.Test()
        
    except Exception as e:
        print(e)
        return 500
