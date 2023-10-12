package main

import (
	"context"
	"fmt"
	"os"

	"dagger.io/dagger"
)

func main() {
	ctx := context.Background()

	// initialize Dagger client
	client, err := dagger.Connect(ctx, dagger.WithLogOutput(os.Stdout), dagger.WithWorkdir(".."))
	if err != nil {
		panic(err)
	}
	defer client.Close()

	path := "usr/src/app"

	// get `golang` image
	myContainer := client.Container().From("python:3").
		WithDirectory(".", client.Host().Directory("."), dagger.ContainerWithDirectoryOpts{Include: []string{"requirements.txt", "app.py"}})

	runner, err := myContainer.
		WithWorkdir(".").
		WithExec([]string{"pip", "install", "--no-cache-dir", "-r", "requirements.txt"}).
		Stderr(ctx)

	if err != nil {
		panic(err)
	}

	flask, err := runner.
		WithWorkdir(".").
		WithExec([]string{"flask", "run", "--host", "0.0.0.0", path}).
		Stderr(ctx)

	if err != nil {
		panic(err)
	}

	fmt.Println(flask)
}
