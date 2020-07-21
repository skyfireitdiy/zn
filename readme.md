# 部署说明

## 一. 准备

需要安装的软件包：
```
docker docker-compose p7zip make
```

## 二. 部署

1. 编译镜像

命令
```bash
make image
```

2. 编写配置文件

在当前目录创建`config.json`文件如下：

```json
{
    "user": "数据库用户名",
    "password": "数据库密码",
    "dsn": "数据库dsn",
    "local_file_save_path": "上传文件存储位置",
    "port": 9393
}
```

3. 启动服务

命令

```bash
docker-compose up -d
```