from ubuntu

env DEBIAN_FRONTEND noninteractive
env PKG_CONFIG_PATH /instantclient_19_6
env LD_LIBRARY_PATH /instantclient_19_6

copy sources.list /etc/apt/
copy instantclient_19_6 /instantclient_19_6

run apt update && apt install -y ca-certificates gcc golang pkg-config libaio1
run go env -w GO111MODULE=on
run go env -w GOPROXY=https://goproxy.cn,direct
run go env -w GOPATH=/root/go
run mkdir /root/zn
run mkdir -p /root/go/pkg

workdir /root/zn