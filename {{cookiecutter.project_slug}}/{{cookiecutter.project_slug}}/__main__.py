"""
Entrypoint for {{cookiecutter.project_name}}
"""

import os
import click

from .util import snake_base, print_version, copy_config, run_snakemake, OrderedCommands


"""CUSTOMISE YOUR LAUNCHER!
Add any extra common command line options to common_options(). 
These are mostly just boilerplate for running Snakemake.

MAIN SCRIPT run()
Add or edit any command line args related to running the main script here, customise the epilog etc.
Currently, the only required input is --input which is simply passed as config to Snakemake.

SUBCOMMAND EXAMPLE config()
Copy the system default config file to working directory.
"""


def common_options(func):
    """Common command line args
    Define common command line args here, and include them with the @common_options decorator below.
    """
    options = [
        click.option('--output', help='Output directory', type=click.Path(),
                     default='{{cookiecutter.project_slug}}.out', show_default=True),
        click.option('--configfile', default='config.yaml', help='Custom config file', show_default=True),
        click.option('--threads', help='Number of threads to use', default=1, show_default=True),
        click.option('--use-conda/--no-use-conda', default=True, help='Use conda for Snakemake rules',
                     show_default=True),
        click.option('--conda-frontend',
                     type=click.Choice(['mamba', 'conda'], case_sensitive=True),
                     default='{{cookiecutter.conda_frontend}}', help='Specify Conda frontend', show_default=True),
        click.option('--conda-prefix', default=snake_base(os.path.join('workflow', 'conda')),
                     help='Custom conda env directory', type=click.Path(), show_default=False),
        click.option('--snake-default', multiple=True,
                     default=['--rerun-incomplete', '--printshellcmds', '--nolock', '--show-failed-logs'],
                     help="Customise Snakemake runtime args", show_default=True),
        click.argument('snake_args', nargs=-1)
    ]
    for option in reversed(options):
        func = option(func)
    return func


@click.group(cls=OrderedCommands)
def cli():
    """For more options, run:
    {{cookiecutter.project_slug}} command --help"""
    pass


help_message_extra = """
\b
CLUSTER EXECUTION:
{{cookiecutter.project_slug}} run ... --profile [profile]
For information on Snakemake profiles see:
https://snakemake.readthedocs.io/en/stable/executing/cli.html#profiles
\b
RUN EXAMPLES:
Required:           {{cookiecutter.project_slug}} run --input [file]
Specify threads:    {{cookiecutter.project_slug}} run ... --threads [threads]
Disable conda:      {{cookiecutter.project_slug}} run ... --no-use-conda 
Change defaults:    {{cookiecutter.project_slug}} run ... --snake-default="-k --nolock"
Add Snakemake args: {{cookiecutter.project_slug}} run ... --dry-run --keep-going --touch
Specify targets:    {{cookiecutter.project_slug}} run ... all print_targets
Available targets:
    all             Run everything (default)
    print_targets   List available targets
"""


@click.command(epilog=help_message_extra, context_settings={"ignore_unknown_options": True})
@click.option('--input', '_input', help='Input file/directory', type=str, required=True)
@common_options
def run(_input, configfile, output, threads, use_conda, conda_frontend, conda_prefix, snake_default,
        snake_args, **kwargs):
    """Run {{cookiecutter.project_name}}"""

    # copy default config file if missing
    copy_config(configfile, system_config=snake_base(os.path.join('config', 'config.yaml')))

    # Config to add or update in configfile
    merge_config = {
        'input': _input,
        'output': output,}

    # run!
    run_snakemake(
        snakefile_path=snake_base(os.path.join('workflow', 'Snakefile')),   # Full path to Snakefile
        configfile=configfile,
        merge_config=merge_config,
        threads=threads,
        use_conda=use_conda,
        conda_frontend=conda_frontend,
        conda_prefix=conda_prefix,
        snake_default_args=snake_default,
        snake_extra=snake_args,
    )


@click.command()
@click.option('--configfile', default='config.yaml', help='Copy template config to file', show_default=True)
def config(configfile, **kwargs):
    """Copy the system default config file"""
    copy_config(configfile, system_config=snake_base(os.path.join('config', 'config.yaml')))


cli.add_command(run)
cli.add_command(config)


def main():
    print_version()
    cli()


if __name__ == '__main__':
    main()
