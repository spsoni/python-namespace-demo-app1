from namespace_demo.main import cli

from namespace_demo.base.base_module import random_name
from namespace_demo.base.shared import hello_world
from namespace_demo.app1.upper_case import upper_case


@cli.command
def app1():
    name = random_name()
    lower_name = upper_case(name)
    hello_world(lower_name)


if __name__ == '__main__':
    cli()
