import os
from setuptools import setup, find_packages


def get_version():
    with open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "{{cookiecutter.project_slug}}",
            "{{cookiecutter.project_slug}}.VERSION",
        )
    ) as f:
        return f.readline().strip()
    

def get_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


def get_data_files():
    data_files = [(".", ["README.md"])]
    return data_files


CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: {{cookiecutter.license}}",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(),
    url="{{cookiecutter.project_url}}",
    python_requires="{{cookiecutter.min_python_version}}",
    description="{{cookiecutter.project_description}}",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    version=get_version(),
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    data_files=get_data_files(),
    py_modules=["{{cookiecutter.project_slug}}"],
    install_requires=[
        "snaketool-utils>=0.0.3",
        "snakemake{{cookiecutter.snakemake_version}}",
        "pyyaml{{cookiecutter.pyyaml_version}}",
        "Click{{cookiecutter.click_version}}",
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.__main__:main"
        ]
    },
    include_package_data=True,
)
