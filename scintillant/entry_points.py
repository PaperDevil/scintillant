"""
scintillant.entry_points.py
~~~~~~~~~~~~~~~~~~~~~~

This module contains the entry-point functions for the scintillant module,
that are referenced in setup.py.
"""
from sys import version_info

from scintillant import about
from scintillant.commands.templates import start_bottle_skill, start_fast_api_skill
from scintillant.commands.testsuite import start_test_suite, start_test_shell
from scintillant.commands.utils import show_testsuite_version

import click


@click.group()
def main() -> None:
    """Main package entry point.

    Delegates to other functions based on user input.
    """
    pass


@main.command()
@click.option('--name', default='bottle-skill-template',
              help="Name of the skill being developed")
def bottle(name):
    """Download the latest skill template"""
    if version_info < (3, 9):
        raise NotImplementedError("This version of framework support on python 3.9 and younger, sorry.")
    start_bottle_skill(skill_name=name)


@main.command()
@click.option('--name', default='fastapi-skill-template',
              help="Name of the skill being developed")
def fastapi(name):
    """Download the latest FastAPI skill template"""
    if version_info < (3, 9):
        raise NotImplementedError("This version of framework support on python 3.9 and younger, sorry.")
    start_fast_api_skill(skill_name=name)


@main.command()
def version():
    """Show version of framework"""
    click.echo('Scintillant Framework ' + about['__version__'])
    show_testsuite_version()


@main.command()
def testsuite():
    """Downloads and runs a test environment for the skill."""
    start_test_suite()


@main.command()
def testshell():
    """Start testing shell in current directory"""
    start_test_shell()
