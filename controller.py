from flask import *
from database import *
from service import *
from functools import *


api = Blueprint("api", __name__)

_service = None

def init_service(config):
    global _service
    _service = Service(config["user"], config["password"], config["dsn"], config["local_db_file"])


err_code = {
    0:"ok",
    1:"user or password error",
    2:"please login",
    4:"user is topped"
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

def make_response(code):
    return {
        "code": code,
        "msg": err_code[code]
    }


@api.route("/login", methods=["POST"])
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
@check_login
def logout():
    del session["user"]
    return make_response(0)


@api.route("/dept", methods=["GET"])
@check_login
def get_department():
    ret = make_response(0)
    ret["data"] = _service.get_all_department()
    return ret
    
@api.route("/patlist", methods=["GET"])
@check_login
def get_patlist():
    req = request.form
    ret = make_response(0)
    if req["name"] != "": 
        ret["data"] = _service.get_patlist_by_name_or_id(req["name"])
    elif req["mine"] == 1:
        ret["data"] = _service.get_patlist_by_user_id(session["user"]["LOGIN_NAME"]) # 责任医生是否是LOGIN_NAME
    else:
        ret["data"] = _service.get_patlist_by_dept(req["dept"])
    return ret


@api.route("/mediatype", methods=["GET"])
@check_login
def get_mediatype():
    ret = make_response(0)
    ret["data"] = _service.get_mediatype()
    return ret


@api.route("/patmediarec", methods=["GET"])
@check_login
def get_patmediarec():
    req = request.form
    ret = make_response(0)
    ret["data"] = _service.get_pat_media_rec(req["pat_id"])
    return ret


@api.route("/patmediarec", methods=["POST"])
@check_login
def add_patmediarec():
    req= request.form
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


@api.route("/patvisit", methods=["GET"])
@check_login
def get_pat_visit():
    req = request.form
    ret = make_response(0)
    ret["data"] = _service.get_pat_visit(req["pat_id"])
    return ret