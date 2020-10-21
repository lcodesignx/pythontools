#!/usr/bin/env python3
import click
import glob

@click.command()
@click.option(
        "--path",
        prompt="Path to search for files",
        help="This is the path to search for files: /tmp",
    )
@click.option(
        "--ftype",
        prompt="Pass in the type of file",
        help="Pass in the file type: i.e csv"
    )

def search(path, ftype):
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found Matches:"))
    for result in results:
        click.echo(click.style(f"{result}"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    search()
