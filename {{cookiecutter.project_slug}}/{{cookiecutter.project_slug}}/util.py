"""MISC FUNCTIONS
You shouldn't need to tweak these much if at all
"""

import sys
import os
import subprocess
import yaml
import click
from shutil import copyfile
from time import localtime, strftime


class OrderedCommands(click.Group):
    """This class will preserve the order of subcommands, which is useful when printing --help"""
    def list_commands(self, ctx: click.Context):
        return list(self.commands)


def snake_base(rel_path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), rel_path)


def print_version():
    with open(snake_base('{{cookiecutter.project_slug}}.VERSION'), 'r') as f:
        version = f.readline()
    click.echo('\n' + '{{cookiecutter.project_name}} version ' + version + '\n', err=True)


def print_citation():
    with open(snake_base('{{cookiecutter.project_slug}}.CITATION'), 'r') as f:
        for line in f:
            click.echo(line, nl=False, err=True)


def msg(err_message):
    tstamp = strftime('[%Y:%m:%d %H:%M:%S] ', localtime())
    click.echo(tstamp + err_message, err=True)


def msg_box(splash, errmsg=None):
    msg('-' * (len(splash) + 4))
    msg(f'| {splash} |')
    msg(('-' * (len(splash) + 4)))
    if errmsg:
        click.echo('\n' + errmsg, err=True)


def default_to_ouput(ctx, param, value):
    """Callback for --configfile; place value in output directory unless specified"""
    if param.default == value:
        return os.path.join(ctx.params['output'], value)
    return value


def copy_config(local_config, system_config=snake_base(os.path.join('config', 'config.yaml'))):
    if not os.path.isfile(local_config):
        msg(f'Copying system default config to {local_config}')
        if len(os.path.dirname(local_config)) > 0:
            os.makedirs(os.path.dirname(local_config), exist_ok=True)
        copyfile(system_config, local_config)
    else:
        msg(f'Config file {local_config} already exists. Using existing config file.')


def read_config(file):
    with open(file, 'r') as stream:
        _config = yaml.safe_load(stream)
    return _config


def write_config(_config, file):
    msg(f'Writing runtime config file to {file}')
    with open(file, 'w') as stream:
        yaml.dump(_config, stream)


"""RUN A SNAKEFILE
Hopefully you shouldn't need to tweak this function at all.
- You must provide a Snakefile, all else is optional
- Highly recommend supplying a configfile and the default snakemake args"""


def run_snakemake(configfile=None, snakefile_path=None, merge_config=None, threads=1, use_conda=False,
                  conda_prefix=None, snake_default=None, snake_args=[]):
    """Run a Snakefile"""
    snake_command = ['snakemake', '-s', snakefile_path]

    # if using a configfile
    if configfile:
        # copy sys default config if not present
        copy_config(configfile)

        # read the config
        snake_config = read_config(configfile)

        # merge in command line config if provided
        if merge_config:
            snake_config.update(merge_config)

            # update config file for Snakemake execution
            write_config(snake_config, configfile)

        snake_command += ['--configfile', configfile]

        # display the runtime configuration
        msg_box('Runtime config', errmsg=yaml.dump(snake_config, Dumper=yaml.Dumper))

    # add threads
    if not '--profile' in snake_args:
        snake_command += ['--jobs', threads]

    # add conda args if using conda
    if use_conda:
        snake_command += ['--use-conda']
        if conda_prefix:
            snake_command += ['--conda-prefix', conda_prefix]

    # add snakemake default args
    if snake_default:
        snake_command += snake_default

    # add any additional snakemake commands
    if snake_args:
        snake_command += list(snake_args)

    # Run Snakemake!!!
    snake_command = ' '.join(str(s) for s in snake_command)
    msg_box('Snakemake command', errmsg=snake_command)
    if not subprocess.run(snake_command, shell=True).returncode == 0:
        msg('ERROR: Snakemake failed')
        sys.exit(1)
    else:
        msg('Snakemake finished successfully')
    return 0