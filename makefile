
run:
	docker run -v${PWD}:/data -e NLS_LANG='SIMPLIFIED CHINESE_CHINA.UTF8' --net=host --rm zn_image python3 main.py

interact:
	docker run -v${PWD}:/data -e NLS_LANG='SIMPLIFIED CHINESE_CHINA.UTF8'  -e NLS_CHARACTERSET='UTF8' --net=host -it --rm zn_image bash



image:docker/*
	cd docker; 7z x ../3rd/dockerfile.7z
	docker build -t zn_image docker
	rm -rvf docker/instantclient_19_6 docker/pkg-config docker/sources.list
