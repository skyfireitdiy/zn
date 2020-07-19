from database import *
import uuid
from datetime import *

class Service:
    def __init__(self, user, password, dsn, localfile):
        self._public_db = new_oracle_database(user, password, dsn)

    def check_password(self, user, password):
        return self._public_db.common_user("select * from COMMON_USER where LOGIN_NAME=:1 and LOGIN_PWD=:2", [user, password])

    @staticmethod
    def make_token():
        return uuid.uuid1().hex

    def get_all_department(self):
        return self._public_db.dict_dept("select * from DICT_DEPT")

    def get_patlist_by_name_or_id(self, name):
        return self._public_db.pat_master("select * from PAT_MASTER where NAME=:1 or PATIENT_ID=:2", [name, name])

    def get_patlist_by_user_id(self, id):
        return self._public_db.pat_master("select * from PAT_MASTER, PAT_VISIT where PAT_VISIT.DUTY_DOCTOR=:1 and PAT_VISIT.PATIENT_ID=PAT_MASTER.PATIENT_ID", [id])

    def get_patlist_by_dept(self, dept):
        return self._public_db.pat_master("select * from PAT_MASTER, PAT_VISIT where PAT_VISIT.DUTY_DEPT=:1 and PAT_VISIT.PATIENT_ID=PAT_MASTER.PATIENT_ID", [dept])

    def get_mediatype(self):
        return self._public_db.dict_media_type("select * from DICT_MEDIA_TYPE")

    def get_pat_media_rec(self, pat_id):
        return self._public_db.pat_media_rec("select * from PAT_MEDIA_REC where PATIENT_ID=:1", [pat_id])

    def get_max_pat_media_rec_id(self):
        result = self._public_db.execute("select max(PAT_MEDIA_REC_ID) from PAT_MEDIA_REC")
        if len(result) == 0 or len(result[0]) == 0 or result[0][0] is None:
            return -1
        return result[0][0]

    def add_pat_media_rec(self, eme_id, pat_id, mediatype, mediatype_id, filename, filetype, filesize, fileduration, create_user_id):
        new_id = self.get_max_pat_media_rec_id() + 1
        self._public_db.execute("insert into PAT_MEDIA_REC(PAT_MEDIA_REC_ID,EME_ID, PATIENT_ID, MEDIA_TYPE, MEDIA_TYPE_ID, FILE_NAME, FILE_TYPE, FILE_SIZE, FILE_DURATION, FILE_PATH,CREATE_TIME,CREATE_USER_ID,UPLOAD_TIME,UPLOAD_USER_ID,STATUS) values(:1, :2, :3, :4, :5, :6,:7, :8, :9, :10, :11, :12, :13, :14, :15)", [
            new_id,
            eme_id,
            pat_id, 
            mediatype,
            mediatype_id,
            filename,
            filetype,
            filesize,
            fileduration,
            "--",
            datetime.now(),
            create_user_id,
            datetime.now(),
            create_user_id,
            "0"
        ])
        return self._public_db.pat_media_rec("select * from PAT_MEDIA_REC where PAT_MEDIA_REC_ID = :1", [new_id])[0]

    def get_pat_visit(self, pat_id):
        return self._public_db.pat_visit("select * from PAT_VISIT where PATIENT_ID=:1", [pat_id])

