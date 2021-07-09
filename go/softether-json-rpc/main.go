package main

import (
	softether "github.com/terassyi/go-softether-api"
	"github.com/terassyi/go-softether-api/methods"
)

func main() {
	api := softether.New("localhost", 5555, "DEFAULT", "softether")
	method := methods.NewGetServerInfo()

	_, err := api.Call(method)
	if err != nil {
		panic(err)
	}
}
