# 赞诺app后台接口设计文档

[TOC]

## API接口说明

文件版本：v1.1

**所有的json格式返回数据均含有`code`，`msg`字段，如果有数据，则会包含`data`字段，操作成功执行时`code`为0，否则会带上错误信息，以下响应描述均描述请求成功时的`data`字段**

### 1. 用户登录

url: /api/login

请求方式：POST

header: 无

请求数据格式：json

请求参数：

| 字段     | 类型   | 描述                               |
| :------- | :----- | :--------------------------------- |
| user     | string | 用户名                             |
| password | string | 密码(**可能需要前台做哈希，待定**) |

响应格式：json

响应参数：

| 字段  | 类型   | 描述                                        |
| :---- | :----- | :------------------------------------------ |
| token | string | Token，后续请求时，该参数需要添加在header中 |

请求示例：

```json
{
    "user":"zhangsan",
    "password":"123456"
}
```

响应示例：

```json
{
    "code":0,
    "msg":"ok",
    "data":{
        "token":"abcd1234"
    }
}
```

### 2. 用户注销

url: /api/logout

请求方式：GET

header: token

请求数据格式：无

请求参数：无

响应格式：json

响应参数：无

响应示例：

```json
{
    "code":0,
    "msg":"ok"
}
```

### 3. 获取科室信息

url: /api/department

请求方式：GET

header: token

请求数据格式：无

请求参数：无

响应格式：json

响应参数：

**暂时没有看到数据库表结构，待定**

### 4. 获取患者列表信息

url: /api/patients

请求方式：GET

header: token

请求数据格式：application/x-www-form-urlencoded

请求参数：

| 字段       | 类型   | 描述                          |
| :--------- | :----- | :---------------------------- |
| pid        | string | 病人id（可选）                |
| name       | string | 病人姓名（可选）              |
| department | string | 科室                          |
| type       | string | 本人:doctor 本科室:department |

响应格式：json

响应参数：

**暂时没有看到数据库表结构，待定**

### 5. 获取文件类型列表

url: /api/filetype

请求方式：GET

header: token

请求数据格式：无

请求参数：无

响应格式：json

响应参数：

**暂时没有看到数据库表结构，待定**

### 6. 上传文件

url: /api/file

请求方式：POST

header: token

请求数据格式：multipart/form-data

请求参数：

| 字段 | 类型   | 描述                             |
| :--- | :----- | :------------------------------- |
| file | file   | 文件                             |
| type | string | 文件类型（**取自数据库，待定**） |
| pid  | string | 用户id                           |

响应格式：json

响应参数：无

响应示例：

```json
{
    "code":0,
    "msg":"ok"
}
```

### 7. 查看文件列表

url: /api/filelist

请求方式：GET

header: token

请求数据格式：无

请求参数：无

响应格式：json

响应参数(列表)：

| 字段     | 类型   | 描述                                |
| :------- | :----- | :---------------------------------- |
| filename | string | 文件名                              |
| type     | string | 文件类型                            |
| id       | string | 文件id                              |
| size     | int    | 文件大小(字节)                      |
| uptime   | string | 文件上传时间（yyyy-MM-dd HH:mm:ss） |


响应示例：

```json
{
    "code":0,
    "msg":"ok",
    "data":[
        {
            "id":"aaaaaaaa",
            "filename":"问诊视频.mp4",
            "filetype":"video",
            "size":"6466469432",
            "uptime":"2020-02-15 03:15:35"
        },
        {
            "id":"bbbbbbbbb",
            "filename":"谈话.mp3",
            "filetype":"audio",
            "size":"5446314",
            "uptime":"2020-02-15 03:15:35"
        },
        {
            "id":"ccccccccc",
            "filename":"CT.jpg",
            "filetype":"image",
            "size":"8512125",
            "uptime":"2020-02-15 03:15:35"
        }
    ]
}
```


### 8. 下载文件

url: /api/file

请求方式：GET

header: token

请求数据格式：multipart/form-data

请求参数：

| 字段 | 类型   | 描述   |
| :--- | :----- | :----- |
| id   | string | 文件id |

响应格式：文件内容

响应参数：无

## 错误码

**待补充**