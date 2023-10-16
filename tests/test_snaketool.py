import subprocess
from pathlib import Path

import pytest


TEST_ROOTDIR = Path(__file__).parent
EXEC_ROOTDIR = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


@pytest.fixture(autouse=True)
def workingdir(tmp_dir, monkeypatch):
    """set the working directory for all tests"""
    monkeypatch.chdir(tmp_dir)


def exec_command(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """executes shell command and returns stdout if completes exit code 0
    Parameters
    ----------
    cmnd : str
      shell command to be executed
    stdout, stderr : streams
      Default value (PIPE) intercepts process output, setting to None
      blocks this."""

    proc = subprocess.Popen(cmnd, shell=True, stdout=stdout, stderr=stderr)
    out, err = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"FAILED: {cmnd}\n{err}")
    return out.decode("utf8") if out is not None else None


def test_snaketool_cli(tmp_dir):
    exec_command("my_snaketool -v")
    exec_command("my_snaketool -h")
    exec_command("my_snaketool run -h")
    exec_command("my_snaketool config -h")
    exec_command("my_snaketool --version")


def test_snaketool_commands(tmp_dir):
    """test Snaketool"""
    exec_command("my_snaketool run --input yeet")
    exec_command("my_snaketool config")
    exec_command("my_snaketool citation")
