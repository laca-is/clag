from click.testing import CliRunner
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clag import cli


def test_build():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['build', 'examples/coffee.maspy', '-o', 'out/coffee.py'])
    print(result)
    assert result.exit_code == 0
    
test_build()