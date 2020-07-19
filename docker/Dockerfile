from ubuntu
run mkdir /data
workdir /data
env DEBIAN_FRONTEND noninteractive
env PKG_CONFIG_PATH /instantclient_19_6
env LD_LIBRARY_PATH /instantclient_19_6
copy sources.list /etc/apt/
copy instantclient_19_6 /instantclient_19_6
run apt update && apt install -y ca-certificates gcc libaio1 python3 python3-pip
run pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip3 install cx_Oracle flask pony
