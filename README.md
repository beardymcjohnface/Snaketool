# Snaketool-lite
Cookiecutter profile for making a Snakemake-based bioinformatics tool, but without the fluff.

__See [Snaketool](https://github.com/beardymcjohnface/Snaketool) for an argparse version with a more detailed Snakemake example.__

## Motivation

Snakemake pipelines are excellent.
However, cloning a pipeline repo every time you want to run an analysis is annoying.
So too is manually punching in the full path to a Snakefile somewhere on your system,
as well as copying and manually updating the config file for your analysis.

Running a Snakemake pipeline via a convenience launcher offers many advantages:
- You can publish it as normal-looking bioinformatics tool and trick NextFlow users into using Snakemake
- It's easier to install, use, and reuse
- You can add subcommands for utility scripts and Snakefiles
- You can write a help message!

## Who is this for?

People who are already familiar with Snakemake and want to create a Snakemake-powered commandline 
tool--or fancier pipelines.

## Usage

To create a new tool from this template, use Cookiecutter and follow the prompts.

```shell
cookiecutter https://github.com/beardymcjohnface/Snaketool-lite.git
```

And here's what you get:

```text
my_snaketool/
├── my_snaketool
│   ├── config
│   │   └── config.yaml
│   ├── __init__.py
│   ├── __main__.py
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

The directories `config/` and `workflow/` contain an example Snakemake pipeline that will work with the example launcher.

## How the launcher works

The launcher first copies the default config file to the working directory which will allow the user to cusomise their
config if they wish. The launcher reads in this config file and combines it with command-line arguments to pass on to 
Snakemake. In this example it only passes on `--input` and `--output`. The Launcher writes a new config file in the 
output directory which will be passed to Snakemake. 

## Installing and testing your tool

For development, cd to your Snaketool directory and install with pip:

```shell
cd snaketool/
pip install -e .
my_snaketool -h
```

## Customising your tool

Check out the [wiki page](https://github.com/beardymcjohnface/Snaketool-lite/wiki) 
for a detailed example on customising your Snaketool.

## Publishing your tool

Add your tool to pip and bioconda like you would any other python package.
Better instructions TBA, watch this space!
