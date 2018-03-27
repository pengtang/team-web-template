from flask.helpers import get_debug_flag
import click
import coverage
import unittest

from project import create_app
from project.config import DevConfig, ProdConfig
# Need to run "export FLASK_APP=run.py" before running "flask test", "flask coverage" etc.

CONFIG = DevConfig if get_debug_flag() else ProdConfig
app = create_app(CONFIG)


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Initiate the db')
    pass


@app.cli.command()
def test():
    """Runs the unit tests without coverage."""
    click.echo("Running tests without coverage")
    pass


@app.cli.command()
def coverage():
    """Runs the unit tests with coverage."""
    click.echo("Running tests with coverage")
    pass


if __name__ == '__main__':
    app.run()
