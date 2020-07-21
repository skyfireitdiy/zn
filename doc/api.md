# 赞诺app后台接口设计文档 {ignore}

[TOC]

## API接口说明

文件版本：v1.1

**所有的json格式返回数据均含有`code`，`msg`字段，如果有数据，则会包含`data`字段，操作成功执行时`code`为0，否则会带上错误信息，以下响应描述均描述请求成功时的`data`字段**

### 1. 用户登录

url: /api/login

请求方式：POST

请求数据格式：json

请求参数：

| 字段     | 描述                            |
| :------- | :------------------------------ |
| user     | 用户名                          |
| password | 密码(密码需要在前台使用MD5哈希) |

响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": {
    "userinfo": {
      "CREATE_TIME": "Tue, 14 May 2019 16:06:11 GMT",
      "DB_NAME": "ANWY",
      "DEFAULT_DEPT_CODE": null,
      "DISPLAY_NAME": "安薇宇",
      "EMPLOYEE_NUMBER": "015",
      "ID": 16,
      "INPUT_CODE": null,
      "IS_STOP": "0",
      "LOGIN_NAME": "ANWY",
      "USER_LEV": null,
      "USER_TITLE_CODE": null,
      "USER_TYPE": "2"
    }
  },
  "msg": "ok"
}
```

<font style="color:red; font-weight:bold">注意：此接口会设置cookies，后续一切操作均需要以此cookie标识用户</font>

### 2. 用户注销

url: /api/logout

请求方式：GET

响应格式：json

响应示例：

```json
{
    "code":0,
    "msg":"ok"
}
```

### 3. 获取科室信息

url: /api/dept

请求方式：GET

响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": [
    {
      "CONDITION_GRADE_CODE": null,
      "CREATE_TIME": "Tue, 03 Dec 2019 10:43:06 GMT",
      "DEPT_ADDRESS": null,
      "DEPT_ALIAS": "急诊妇产科",
      "DEPT_CODE": "420214",
      "DEPT_NAME": "急诊妇产科",
      "DEPT_PHONE": null,
      "EMERGENCY_AREA_CODE": null,
      "HOSPITAL_AREA_CODE": "600016",
      "ID": 86,
      "INPUT_CODE": "JZFCK",
      "INTERNAL_OR_SERGERY": null,
      "IS_EXAM": "0",
      "IS_LAB": "0",
      "IS_PHARMACY": "0",
      "IS_STOP": "0",
      "NURSING_GRADE_CODE": null,
      "OUTP_OR_INP": "1",
      "SERIAL_NO": 6
    }
  ],
  "msg": "ok"
}
```

### 4. 获取患者列表信息

url: /api/patlist

请求方式：GET

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段 | 描述                |
| :--- | :------------------ |
| name | 病人ID/姓名（可选） |
| dept | 科室（可选）        |
| mine | 本人:1 本科室:0     |

`name`的优先级最高，然后是`mine`，最后是`dept`

响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": [
    {
      "ADDRESS": "甘肃省天水市世纪金花小区B座112座",
      "ALLERGIC_HISTORY": null,
      "BIRTH_DATE": "Mon, 28 Mar 1966 00:00:00 GMT",
      "BIRTH_PLACE": null,
      "CARD_NO": "1800567544",
      "CHARGE_TYPE": "D",
      "CITIZENSHIP": "CN",
      "CREATE_TIME": "Tue, 07 May 2019 17:06:03 GMT",
      "IDENTITY": "D",
      "ID_NO": "620502196603285141",
      "ID_TYPE": "0",
      "INP_NO": "F97432",
      "INSURANCE_NO": null,
      "INSURANCE_TYPE": null,
      "LAST_VISIT_DATE": "Tue, 15 Oct 2019 00:00:00 GMT",
      "MARITAL_STATUS": null,
      "NAME": "杨热闹",
      "NAME_PHONETIC": "YANG RE NAO",
      "NATION": "01",
      "NEXT_OF_KIN": "罗双平",
      "NEXT_OF_KIN_ADDR": "同上",
      "NEXT_OF_KIN_PHONE": "13919649002",
      "NEXT_OF_KIN_ZIP_CODE": "740000",
      "OCCUPATION": null,
      "OPERATOR": "006",
      "PATIENT_ID": "1800567544",
      "PATIENT_PROPERTY": "0",
      "PHONE_NUMBER": null,
      "PHONE_NUMBER_BUSINESS": null,
      "RELATIONSHIP": null,
      "SEX": "1",
      "UNIT_IN_CONTRACT": null,
      "VIP_INDICATOR": "0",
      "ZIP_CODE": "740000"
    }
  ],
  "msg": "ok"
}
```


### 5. 获取文件类型列表

url: /api/mediatype

请求方式：GET

请求数据格式：application/x-www-form-urlencoded

响应格式：json

响应参数：

```json
{
  "code": 0,
  "data": [
    {
      "CREATE_TIME": "Wed, 13 May 2020 00:00:00 GMT",
      "IS_STOP": "0",
      "MEDIA_TYPE": "PIC",
      "MEDIA_TYPE_ID": 1,
      "SERIAL_NO": 1,
      "SUB_TYPE_CODE": "1",
      "SUB_TYPE_NAME": "心电图"
    },
    {
      "CREATE_TIME": "Wed, 13 May 2020 00:00:00 GMT",
      "IS_STOP": "0",
      "MEDIA_TYPE": "PIC",
      "MEDIA_TYPE_ID": 2,
      "SERIAL_NO": 2,
      "SUB_TYPE_CODE": "2",
      "SUB_TYPE_NAME": "CT胶片"
    }
  ],
  "msg": "ok"
}
```

### 6. 查询患者的文件列表

url: /api/patmediarec

请求方式：GET

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段   | 描述   |
| :----- | :----- |
| pat_id | 病人ID |

响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": [
    {
      "CREATE_TIME": "Mon, 20 Jul 2020 15:48:28 GMT",
      "CREATE_USER_ID": 16,
      "EME_ID": "402eed1ab90940ac8356471239705284",
      "FILE_DURATION": 360000,
      "FILE_NAME": "我的文件.png",
      "FILE_PATH": "./data/edb48d64caa011ea98e8ace010a7306eyarn.lock",
      "FILE_SIZE": 36504,
      "FILE_TYPE": "png",
      "MEDIA_TYPE": "PIC",
      "MEDIA_TYPE_ID": "1",
      "PATIENT_ID": "0000191951",
      "PAT_MEDIA_REC_ID": 0,
      "STATUS": "1",
      "UPLOAD_TIME": "Mon, 20 Jul 2020 15:51:51 GMT",
      "UPLOAD_USER_ID": 16
    }
  ],
  "msg": "ok"
}
```

### 7. 查看病人就诊记录

url: /api/patvisit

请求方式：GET

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段   | 描述   |
| :----- | :----- |
| pat_id | 病人ID |

响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": [
    {
      "BED_NAME": "抢+3",
      "BED_NO": "4202030103",
      "CONDITION_GRADE_CODE": null,
      "CREATE_DATE": "Thu, 28 May 2020 10:43:00 GMT",
      "DIAGNOSIS": null,
      "DUTY_DEPT": "420203",
      "DUTY_DOCTOR": "0000",
      "DUTY_NURSE": null,
      "EME_ID": "402eed1ab90940ac8356471239705284",
      "EMR_NO": null,
      "FIRST_VISIT_DEPT": "420203",
      "FIRST_VISIT_DOCTOR": "0000",
      "ID": 13361,
      "INPATIENT_DEPT": null,
      "IN_DEPT_OPERATOR": "0000",
      "IN_DEPT_TIME": "Thu, 28 May 2020 10:43:00 GMT",
      "IN_OBSERVATION_TIME": null,
      "IN_RESUSCITATION_TIME": null,
      "IS_CONCERNED": "1",
      "NAME": "杨天磊",
      "NURSING_GRADE_CODE": null,
      "OUT_DEPT_OPERATOR": null,
      "OUT_DEPT_TIME": null,
      "OUT_DEPT_WHERE": null,
      "PATIENT_ID": "0000191951",
      "REGISTER_ID": 14461,
      "TRIAGE_ID": 14861,
      "VISIT_NO": "14461",
      "WHERE_NOTE": null
    }
  ],
  "msg": "ok"
}
```


### 8. 上传文件信息

url: /api/patmediarec

请求方式：POST

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段         | 描述         |
| :----------- | :----------- |
| eme_id       | 就诊ID       |
| pat_id       | 患者ID       |
| mediatype    | PIC          |
| mediatype_id | 媒体类型的ID |
| filename     | 文件名       |
| filetype     | 文件类型     |
| fileduration | 文件时长     |
| filesize     | 文件大小     |


响应格式：json

响应示例：

```json
{
  "code": 0,
  "data": [
    {
      "CREATE_TIME": "Mon, 20 Jul 2020 15:48:28 GMT",
      "CREATE_USER_ID": 16,
      "EME_ID": "402eed1ab90940ac8356471239705284",
      "FILE_DURATION": 360000,
      "FILE_NAME": "中文文件名",
      "FILE_PATH": "--",
      "FILE_SIZE": 36504,
      "FILE_TYPE": "png",
      "MEDIA_TYPE": "PIC",
      "MEDIA_TYPE_ID": "1",
      "PATIENT_ID": "0000191951",
      "PAT_MEDIA_REC_ID": 0,
      "STATUS": "0",
      "UPLOAD_TIME": "Mon, 20 Jul 2020 15:48:28 GMT",
      "UPLOAD_USER_ID": 16
    }
  ],
  "msg": "ok"
}
```


### 9. 删除文件信息

url: /api/patmediarec

请求方式：DELETE

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段             | 描述       |
| :--------------- | :--------- |
| pat_media_rec_id | 文件信息ID |


响应格式：json

响应示例：

```json
{
  "code": 0,
  "msg": "ok"
}
```

### 10. 文件上传

url: /api/upload

请求方式：POST

请求数据格式：multipart/form-data

请求参数：

| 字段             | 描述       |
| :--------------- | :--------- |
| pat_media_rec_id | 文件信息ID |
| file             | 上传的文件 |

响应格式：json

响应示例：

```json
{
    "code": 0,
    "msg": "ok"
}
```

### 11. 下载文件

url: /api/file

请求方式：GET

请求数据格式：multipart/form-data

请求参数：

| 字段             | 描述       |
| :--------------- | :--------- |
| pat_media_rec_id | 文件信息ID |

响应格式：文件流

响应示例：

## 错误码

注意：错误码只在返回200的时候才有意义，如果服务器返回状态码不是200，请检查参数是否符合要求。

| 错误码 | 含义               |
| :----: | :----------------- |
|   0    | 成功               |
|   1    | 用户名或者密码错误 |
|   2    | 未登录             |
|   3    | 未找到记录         |
|   4    | 用户被禁用         |
|   5    | 文件数量错误       |
|   6    | 已经被上传         |
|   7    | 未上传             |
|   8    | 找不到文件         |

