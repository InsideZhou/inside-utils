package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/urfave/cli/v2"
)

func main() {
	var defaultLen = 16
	alphanumeric := "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	app := &cli.App{
		Name:  "randstr",
		Usage: "Random alphanumeric string generator",
		Action: func(context *cli.Context) error {
			var length = defaultLen
			var err error = nil

			if context.Args().Present() {
				l, e := strconv.ParseInt(context.Args().First(), 10, 0)
				length = int(l)
				err = e
			}

			if err != nil {
				log.Fatalln("invalid string length")
				return nil
			}

			var letters []string
			exampleLength := len(alphanumeric)

			rand.Seed(time.Now().UnixNano())
			for i := 0; i < length; i++ {
				letters = append(letters, string(alphanumeric[rand.Intn(exampleLength)]))
			}

			fmt.Print(strings.Join(letters, ""))

			return nil
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
