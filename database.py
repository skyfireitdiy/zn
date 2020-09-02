import cx_Oracle
import threading


class Database:
    def __init__(self, user, password, dsn):
        self._user = user
        self._password = password
        self._dsn = dsn
        self._connection_pool = cx_Oracle.SessionPool(
            user=self._user, password=self._password, dsn=self._dsn, min=1, max=500, increment=1)

    def execute(self, *args, **kwargs):
        try:
            connection = self._connection_pool.acquire()
            cur = connection.cursor()
            result = cur.execute(*args, **kwargs)
            ret = []
            if result is not None:
                for row in result:
                    ret.append(row)
            cur.close()
            self._connection_pool.release(connection)
            return ret
        except Exception as e:
            self._connection_pool.release(connection)
            raise e

    def common_user(self, *args, **kwargs):
        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "ID":                      r[0],
                "USER_TYPE":               r[1],
                "LOGIN_NAME":              r[2],
                "LOGIN_PWD":               r[3],
                "DB_NAME":                 r[4],
                "DB_PWD":                  r[5],
                "DISPLAY_NAME":            r[6],
                "INPUT_CODE":              r[7],
                "EMPLOYEE_NUMBER":         r[8],
                "USER_TITLE_CODE":         r[9],
                "USER_LEV":                r[10],
                "DEFAULT_DEPT_CODE":       r[11],
                "CREATE_TIME":             r[12],
                "IS_STOP":                 r[13],
            })
        
        
        return ret

    def dict_media_type(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "MEDIA_TYPE_ID": r[0],
                "SERIAL_NO": r[1],
                "MEDIA_TYPE": r[2],
                "SUB_TYPE_CODE": r[3],
                "SUB_TYPE_NAME": r[4],
                "CREATE_TIME": r[5],
                "IS_STOP": r[6],
            })
        
        
        return ret

    def dict_dept(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "ID": r[0],
                "SERIAL_NO": r[1],
                "DEPT_CODE": r[2],
                "DEPT_NAME": r[3],
                "DEPT_ALIAS": r[4],
                "DEPT_PHONE": r[5],
                "DEPT_ADDRESS": r[6],
                "INPUT_CODE": r[7],
                "INTERNAL_OR_SERGERY": r[8],
                "OUTP_OR_INP": r[9],
                "IS_PHARMACY": r[10],
                "IS_EXAM": r[11],
                "IS_LAB": r[12],
                "EMERGENCY_AREA_CODE": r[13],
                "HOSPITAL_AREA_CODE": r[14],
                "CREATE_TIME": r[15],
                "IS_STOP": r[16],
                "CONDITION_GRADE_CODE": r[17],
                "NURSING_GRADE_CODE": r[18],
            })
        
        
        return ret

    def pat_master(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "PATIENT_ID": r[0],
                "CARD_NO": r[1],
                "INP_NO": r[2],
                "NAME": r[3],
                "NAME_PHONETIC": r[4],
                "SEX": r[5],
                "BIRTH_DATE": r[6],
                "BIRTH_PLACE": r[7],
                "CITIZENSHIP": r[8],
                "NATION": r[9],
                "ID_NO": r[10],
                "IDENTITY": r[11],
                "CHARGE_TYPE": r[12],
                "UNIT_IN_CONTRACT": r[13],
                "ADDRESS": r[14],
                "ZIP_CODE": r[15],
                "PHONE_NUMBER": r[16],
                "PHONE_NUMBER_BUSINESS": r[17],
                "NEXT_OF_KIN": r[18],
                "RELATIONSHIP": r[19],
                "NEXT_OF_KIN_ADDR": r[20],
                "NEXT_OF_KIN_ZIP_CODE": r[21],
                "NEXT_OF_KIN_PHONE": r[22],
                "LAST_VISIT_DATE": r[23],
                "VIP_INDICATOR": r[24],
                "OPERATOR": r[25],
                "CREATE_TIME": r[26],
                "INSURANCE_TYPE": r[27],
                "INSURANCE_NO": r[28],
                "OCCUPATION": r[29],
                "MARITAL_STATUS": r[30],
                "ALLERGIC_HISTORY": r[31],
                "PATIENT_PROPERTY": r[32],
                "ID_TYPE": r[33],
            })
        
        
        return ret

    def pat_visit(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "ID": r[0],
                "EME_ID": r[1],
                "TRIAGE_ID": r[2],
                "REGISTER_ID": r[3],
                "IN_DEPT_TIME": r[4],
                "IN_DEPT_OPERATOR": r[5],
                "FIRST_VISIT_DEPT": r[6],
                "FIRST_VISIT_DOCTOR": r[7],
                "DUTY_DEPT": r[8],
                "DUTY_DOCTOR": r[9],
                "DUTY_NURSE": r[10],
                "BED_NO": r[11],
                "CONDITION_GRADE_CODE": r[12],
                "NURSING_GRADE_CODE": r[13],
                "IN_RESUSCITATION_TIME": r[14],
                "IN_OBSERVATION_TIME": r[15],
                "OUT_DEPT_TIME": r[16],
                "OUT_DEPT_WHERE": r[17],
                "WHERE_NOTE": r[18],
                "OUT_DEPT_OPERATOR": r[19],
                "CREATE_DATE": r[20],
                "PATIENT_ID": r[21],
                "IS_CONCERNED": r[22],
                "VISIT_NO": r[23],
                "NAME": r[24],
                "BED_NAME": r[25],
                "DIAGNOSIS": r[26],
                "INPATIENT_DEPT": r[27],
                "EMR_NO": r[28],
            })
        
        
        return ret

    def pat_media_rec(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "PAT_MEDIA_REC_ID": r[0],
                "EME_ID": r[1],
                "PATIENT_ID": r[2],
                "MEDIA_TYPE": r[3],
                "MEDIA_TYPE_ID": r[4],
                "FILE_NAME": r[5],
                "FILE_TYPE": r[6],
                "FILE_SIZE": r[7],
                "FILE_DURATION": r[8],
                "FILE_PATH": r[9],
                "CREATE_TIME": r[10],
                "CREATE_USER_ID": r[11],
                "UPLOAD_TIME": r[12],
                "UPLOAD_USER_ID": r[13],
                "STATUS": r[14],
            })
        
        
        return ret

    def pat_visit(self, *args, **kwargs):

        result = self.execute(*args, **kwargs)
        ret = []
        if result is None:
            return ret
        for r in result:
            ret.append({
                "ID": r[0],
                "EME_ID": r[1],
                "TRIAGE_ID": r[2],
                "REGISTER_ID": r[3],
                "IN_DEPT_TIME": r[4],
                "IN_DEPT_OPERATOR": r[5],
                "FIRST_VISIT_DEPT": r[6],
                "FIRST_VISIT_DOCTOR": r[7],
                "DUTY_DEPT": r[8],
                "DUTY_DOCTOR": r[9],
                "DUTY_NURSE": r[10],
                "BED_NO": r[11],
                "CONDITION_GRADE_CODE": r[12],
                "NURSING_GRADE_CODE": r[13],
                "IN_RESUSCITATION_TIME": r[14],
                "IN_OBSERVATION_TIME": r[15],
                "OUT_DEPT_TIME": r[16],
                "OUT_DEPT_WHERE": r[17],
                "WHERE_NOTE": r[18],
                "OUT_DEPT_OPERATOR": r[19],
                "CREATE_DATE": r[20],
                "PATIENT_ID": r[21],
                "IS_CONCERNED": r[22],
                "VISIT_NO": r[23],
                "NAME": r[24],
                "BED_NAME": r[25],
                "DIAGNOSIS": r[26],
                "INPATIENT_DEPT": r[27],
                "EMR_NO": r[28],
            })
        
        
        return ret


def new_oracle_database(user, password, dsn):
    return Database(user, password, dsn)


if __name__ == "__main__":
    db = new_oracle_database("username", "password", "ip:port/orcl")
    result = db.pat_master(
        "select * from PAT_MASTER where PATIENT_ID='1800567544'")
    print(result)
    result = db.pat_master(
        "select * from PAT_MASTER where NAME=N'杨热闹'")
    print(result)
