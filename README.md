# Snaketool

[![CI](https://github.com/beardymcjohnface/Snaketool/actions/workflows/python-app.yml/badge.svg)](https://github.com/beardymcjohnface/Snaketool/actions/workflows/python-app.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Cookiecutter profile for making a Snakemake-based bioinformatics tool.

__See [Nektool](https://github.com/beardymcjohnface/Nektool) for a NextFlow-based template__

## Motivation

Writing reliable command line tools requires a lot of boilerplate to ensure input and generated files are valid, 
catch errors with subprocesses, log stderr messages etc. It's very time-consuming and annoying.
Snakemake does a lot of heavy lifting in this regard and is an obvious alternative to a command line tool.

While Snakemake pipelines are excellent, cloning a pipeline repo every time you want to run an analysis is also annoying.
So too is manually punching in the full path to a Snakefile somewhere on your system,
as well as copying and manually updating the config file for your analysis.

Building a Snakemake pipeline with a convenience launcher offers the best of both worlds:
- Developing command line applications is quicker and easier
- Installing, running, and rerunning is easier and more convenient
- You can have subcommands for utility scripts and Snakefiles
- You can trick NextFlow users into running Snakemake
- Your pipelines have help messages!

## Who is this for?

People who are already familiar with Snakemake and want to create either a Snakemake-powered commandline 
tool or make their pipelines fancier and more user-friendly.

## Citation

This template is published in Plos Computational Biology: 

[https://doi.org/10.1371/journal.pcbi.1010705](https://doi.org/10.1371/journal.pcbi.1010705)

## Usage

Install Cookiecutter if you don't already have it.

```shell
conda create -n cookiecutter -c conda-forge cookiecutter 
conda activate cookiecutter
```

Download the template with Cookiecutter and follow the prompts

```shell
cookiecutter https://github.com/beardymcjohnface/Snaketool.git
```

And here's what you get:

```text
my_snaketool/
├── my_snaketool
│   ├── config
│   │   └── config.yaml
│   ├── __init__.py
│   ├── __main__.py
│   ├── util.py
│   ├── my_snaketool.LICENSE
│   ├── my_snaketool.VERSION
│   └── workflow
│       └── Snakefile
└── setup.py
```

The file `__main__.py` is the entry point.
Once installed with pip it will be accessible on command line, in this example as `my_snaketool`.
Customise this file to add your own commandline options, help message etc.
If you only have one Snakefile you wish to run then this file will need very little customisation.
If you're happy only using --input and --output you don't have to do anything!

The directories `config/` and `workflow/` contain an example Snakemake pipeline that will work with the example launcher.

## How the launcher works

The launcher first copies the default config file to the working directory which will allow the user to cusomise their
config if they wish. The launcher reads in this config file and combines it with command-line arguments. 
In this example it only has two config-related options to pass: `--input` and `--output`. 
The Launcher updates the config file with these options before passing it to Snakemake.  
Most of the other command line arguments are boilerplate for running Snakemake and do not require much if any customisation.

## Customising your tool

__[Check out the wiki page](https://github.com/beardymcjohnface/Snaketool/wiki/Customising-your-Snaketool) for a detailed example on customising your Snaketool.__

## Installing and testing your tool

For development, cd to your Snaketool directory and install with pip:

```shell
cd snaketool/
pip install -e .
my_snaketool --help
my_snaketool run --help
```

Test run the template:

```shell
my_snaketool run --input yeet
```

## Publishing your tool

__[Check out the wiki page](https://github.com/beardymcjohnface/Snaketool/wiki/Publishing-your-Snaketool) for a detailed look at publishing your tool to PyPI and Conda__
