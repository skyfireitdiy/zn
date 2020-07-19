## 登录

### 成功登录
```bash {cmd}
curl http://127.0.0.1:9393/api/login -v -X POST -d '{"user":"ANWY", "password":"5fa285e1bebea6623e33afc4a1fbd5"}' -s
```

### 失败登录

```bash {cmd}
curl http://127.0.0.1:9393/api/login -X POST -d '{"user":"ANWY", "password":"wrong password"}' -s
```

## 注销

```bash{cmd}
curl http://127.0.0.1:9393/api/logout -v -s -H 'cookie:session=eyJ1c2VyIjp7fX0.XxMCyw.XBfBWmsvNBHPgaKQxU9WLedhryg'
```

## 获取科室信息

```bash{cmd}
curl http://127.0.0.1:9393/api/dept -s -H 'token: 12e39e52c8f011eab320ace010a7306e'
```