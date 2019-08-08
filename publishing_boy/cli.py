# -*- coding: utf-8 -*-
from publishing_boy.publishing_boy import process
from publishing_boy.process import create_content_folder

"""Console script for publishing_boy."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for publishing_boy."""
    click.echo("Replace this message by putting your code into "
               "publishing_boy.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    folder = '' # from click arguments

    destination_dir = ''
    create_content_folder(destination_dir)

    report = process(folder)

    from pprint import pprint
    pprint(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
