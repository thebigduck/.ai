import os
import sys
import json
import tempfile
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_cli import cli


def test_ai_init_creates_dirs():
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            cli.ai_init(None)
            base = os.path.join(tmp, '.ai')
            expected = [
                '0-ai-config',
                '1-context',
                '2-technical-design',
                '3-development',
                '4-acceptance',
            ]
            assert cli.DEFAULT_DIRS == expected
            for d in expected:
                assert os.path.isdir(os.path.join(base, d))
        finally:
            os.chdir(cwd)


def test_ai_migrate_and_validate():
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            with open('README.md', 'w') as f:
                f.write('# Sample\nA sample project.')
            cli.ai_migrate(None)
            assert os.path.isfile(os.path.join('.ai', '0-ai-config', 'ai-config.json'))
            assert os.path.isfile(os.path.join('.ai', '1-context', 'project_context.md'))
            exit_code = cli.ai_validate(None)
            assert exit_code == 0
            with open(os.path.join('.ai', '0-ai-config', 'ai-config.json')) as f:
                data = json.load(f)
            assert data['project_name'] == 'Sample'
        finally:
            os.chdir(cwd)

