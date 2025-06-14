from setuptools import setup, find_packages

setup(
    name='ads-cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ai-init=ai_cli.init_cmd:main',
            'ai-migrate=ai_cli.migrate_cmd:main',
            'ai-validate=ai_cli.validate_cmd:main',
            'gitmcp=ai_cli.gitmcp_cmd:main',
        ],
    },
)
