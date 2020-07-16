
build:src/controller/* src/database/* src/models/* src/service/* src/main.go
	docker run -v${PWD}/src:/root/zn -v${PWD}/pkg:/root/go/pkg --rm zn_image go build -o zn

run:zn
	docker run -v${PWD}/src:/root/zn -v${PWD}/pkg:/root/go/pkg --rm zn_image ./zn

test:
	docker run -v${PWD}/src:/root/zn -v${PWD}/pkg:/root/go/pkg --rm zn_image go test ./...

image:docker/*
	cd docker; 7z x ../3rd/dockerfile.7z
	docker build -t zn_image docker
