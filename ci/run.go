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

	src := client.Host().Directory(".", dagger.HostDirectoryOpts{
		Exclude: []string{"Dockerfile", "go.mod", "go.sum", ".gitignore", ".git", ".github/"},
	})

	entries, err := src.Entries(ctx)
	// if err != nil {
	// 	return nil, fmt.Errorf("failed to get cache files: %w", err)
	// }

	fmt.Print(entries)
	// get `golang` image
	myContainer := client.Container().From("python:3")

	// mount cloned repository into `golang` image
	myContainer = myContainer.WithDirectory(".", src).WithWorkdir(".")

	path := "build/"
	output := myContainer.Directory(path)

	myContainer = myContainer.WithExec([]string{"pip", "install", "--no-cache-dir", "-r", "requirements.txt"})

	myContainer = myContainer.WithExec([]string{"flask", "run", "--host", "0.0.0.0", path})

	// get reference to build output directory in container
	// output := myContainer.Directory(path)

	// write contents of container build/ directory to the host
	_, err = output.Export(ctx, path)
	if err != nil {
		panic(err)
	}

}
