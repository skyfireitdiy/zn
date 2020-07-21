from flask import *
from controller import *
from config_manager import *
import os

if __name__ == '__main__':
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    app = Flask(__name__)
    app.secret_key = uuid.uuid1().hex
    config = load_config("config.json")
    os.makedirs(config["local_file_save_path"], exist_ok=True)
    init_service(config)
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=config["port"], debug=False)
