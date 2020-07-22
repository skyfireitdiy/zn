from flask import *
from database import *
from service import *
from functools import *
from werkzeug.utils import *


api = Blueprint("api", __name__)

_service = None
_config = None


def init_service(config):
    global _service, _config
    _service = Service(config["user"], config["password"],
                       config["dsn"])
    _config = config


err_code = {
    0: "ok",
    1: "user or password error",
    2: "please login",
    3: "record not found",
    4: "user is topped",
    5: "file count error",
    6: "already uploaded", 
    7: "file not uploaded",
    8: "file not found",
}


def check_login(f):
    @wraps(f)
    def r(*args, **kwargs):
        if session.new:
            return make_response(2)
        if "user" not in session:
            return make_response(2)
        return f(*args, **kwargs)
    return r

def logger(f):
    @wraps(f)
    def r(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            current_app.logger.error(e)
            return None
    return r

def make_response(code):
    return {
        "code": code,
        "msg": err_code[code]
    }


@api.route("/login", methods=["POST"])
@logger
def login():
    req = request.form
    userinfo = _service.check_password(req["user"], req["password"])
    if len(userinfo) != 0:
        if userinfo[0]["IS_STOP"] == "1":
            return make_response(4)
        session["user"] = userinfo[0]
        ret = make_response(0)
        del userinfo[0]["DB_PWD"]
        del userinfo[0]["LOGIN_PWD"]
        ret["data"] = {
            "userinfo": userinfo[0]
        }
        return ret
    return make_response(1)


@api.route("/logout", methods=["GET"])
@logger
@check_login
def logout():
    del session["user"]
    return make_response(0)


@api.route("/dept", methods=["GET"])
@logger
@check_login
def get_department():
    ret = make_response(0)
    ret["data"] = _service.get_all_department()
    return ret


@api.route("/patlist", methods=["GET"])
@logger
@check_login
def get_patlist():
    req = request.args
    ret = make_response(0)
    if "name" in req and req["name"] != "":
        ret["data"] = _service.get_patlist_by_name_or_id(req["name"])
    elif "mine" in req and req["mine"] == 1:
        ret["data"] = _service.get_patlist_by_user_id(
            session["user"]["LOGIN_NAME"])  # 责任医生是否是LOGIN_NAME
    else:
        ret["data"] = _service.get_patlist_by_dept(req["dept"])
    return ret


@api.route("/mediatype", methods=["GET"])
@logger
@check_login
def get_mediatype():
    ret = make_response(0)
    ret["data"] = _service.get_mediatype()
    return ret


@api.route("/patmediarec", methods=["GET"])
@logger
@check_login
def get_patmediarec():
    req = request.args
    ret = make_response(0)
    ret["data"] = _service.get_pat_media_rec(req["pat_id"])
    return ret


@api.route("/patmediarec", methods=["POST"])
@logger
@check_login
def add_patmediarec():
    req = request.form
    ret = make_response(0)
    ret["data"] = _service.add_pat_media_rec(
        req["eme_id"],
        req["pat_id"],
        req["mediatype"],
        req["mediatype_id"],
        req["filename"],
        req["filetype"],
        int(req["filesize"]),
        int(req["fileduration"]),
        int(session["user"]["ID"])
    )
    return ret


@api.route("/patmediarec", methods=["DELETE"])
@logger
@check_login
def del_patmediarec():
    req = request.args
    del_result = _service.del_pat_media_rec(req["pat_media_rec_id"])
    if del_result == 1:
        return make_response(3)
    return make_response(0)


@api.route("/upload", methods=["POST"])
@logger
@check_login
def upload():
    global _config
    req = request.form
    file = request.files["file"]
    result = _service.get_pat_media_rec_by_id(req["pat_media_rec_id"])
    if len(result) != 1:
        return make_response(3)
    if result[0]["STATUS"] == "1":
        return make_response(6)
    filename = os.path.join(_config["local_file_save_path"],
                            _service.make_token() + secure_filename(file.filename))
    file.save(filename)
    ret = make_response(0)
    ret["data"] = _service.update_pat_media_rec(
        req["pat_media_rec_id"], filename)
    return ret

@api.route("/file", methods=["GET"])
@logger
@check_login
def download_file():
    req = request.args
    result = _service.get_pat_media_rec_by_id(req["pat_media_rec_id"])
    if len(result) != 1:
        return make_response(3)
    if result[0]["STATUS"] != "1":
        return make_response(7)
    filename = result[0]["FILE_PATH"]
    if not os.path.exists(filename):
        return make_response(8)
    filename = os.path.basename(result[0]["FILE_PATH"])
    return send_from_directory(_config["local_file_save_path"], filename, as_attachment=True)


@api.route("/patvisit", methods=["GET"])
@logger
@check_login
def get_pat_visit():
    req = request.args
    ret = make_response(0)
    ret["data"] = _service.get_pat_visit(req["pat_id"])
    return ret
