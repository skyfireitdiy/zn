package controller

import "com.skyfire.zn/service"

type ControllerImpl struct {
	service *service.Service
}

func (c ControllerImpl) PostLogin() {

}

func NewController(service *service.Service) Controller {
	return ControllerImpl{
		service: service,
	}
}
