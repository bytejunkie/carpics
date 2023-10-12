import sys

import anyio
import dagger


async def main():
    config = dagger.Config(log_output=sys.stdout)

    # initialize Dagger client
    async with dagger.Connection(config) as client:
        # use a python:3.11-slim container
        # mount the source code directory on the host
        # at /src in the container
        source = (
            client.container()
            .from_("python:3.11-slim")
            .with_directory(
                ".",
                client.host().directory("."),
                exclude=[".github/", ".vscode/", "ci/", "src/", ".gitignore", "Dockerfile", "go.*"],
            )
        )
        
        # set the working directory in the container
        # install application dependencies
        runner = source.with_workdir(".").with_exec(["pip", "install", "-r", "requirements.txt"])

        # execute
        out = await runner.with_exec(["flask", "run", "--host", "0.0.0.0"]).stderr()
        
        print(out)

    # print output
    print(f"Hello from Dagger and {version}")


anyio.run(main)