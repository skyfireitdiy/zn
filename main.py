from flask import *
from controller import *
from config_manager import *
import os
import logging
from logging.handlers import *

if __name__ == '__main__':
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    app = Flask(__name__)
    app.secret_key = uuid.uuid1().hex
    config = load_config("config.json")
    os.makedirs(config["local_file_save_path"], exist_ok=True)
    os.makedirs(config["log_file_path"], exist_ok=True)

    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        os.path.join(config["log_file_path"], "zn.log"), when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)

    
    init_service(config)
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=config["port"], debug=False)
