import click
from .decorators import config_group
import yaml


# Core wq CLI
@config_group()
@click.option(
    '-c', '--config',
    default='wq.yml',
    type=click.Path(),
    help='Path to configuration file (default is wq.yml).'
)
@click.pass_context
def wq(ctx, config):
    """
    wq is a suite of command line utilities for building citizen science apps.
    """
    if ctx.obj:
        # Allow for multiple invocations without resetting context
        return

    try:
        conf = Config(yaml.load(open(config)))
        conf.filename = config
    except IOError:
        if config != "wq.yml":
            raise
        conf = Config()
    ctx.obj = conf
    ctx.default_map = conf


class Config(dict):
    filename = None

wq.pass_config = click.make_pass_decorator(Config)


# Load custom commands from other modules
from pkg_resources import iter_entry_points
module_names = []
for module in iter_entry_points(group='wq', name=None):
    module_names.append(module.name)
    module.load()

# Update help text with list of installed modules
if module_names:
    wq.help += " Installed modules: " + ", ".join(sorted(module_names))
