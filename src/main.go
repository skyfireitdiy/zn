package main

import (
	"com.skyfire.zn/controller"
	"com.skyfire.zn/database"

	"com.skyfire.zn/service"
	"github.com/kataras/iris"
	"github.com/kataras/iris/mvc"
	"github.com/sirupsen/logrus"
)

func main() {
	app := iris.New()

	db, err := database.NewDatabase("app/app123456/114.115.140.157:1521/orcl", "./fileinfo.db")
	if err != nil {
		logrus.Error(err.Error())
	}
	service := service.NewService(db)
	c := controller.NewController(&service)

	mvc.Configure(app.Party("/api"), func(app *mvc.Application) {
		app.Handle(c)
	})
	app.Run(
		iris.Addr("localhost:8080"),
	)
}
