import argparse
import json
import os
import sys

DEFAULT_DIRS = [
    '0-ai-config',
    '1-context',
    '2-technical-design',
    '3-development',
    '4-acceptance'
]

SCHEMA = {
    "type": "object",
    "required": ["projectName", "description", "primaryLanguage", "aiPreferences"],
    "properties": {
        "projectName": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "primaryLanguage": {"type": "string"},
        "frameworks": {
            "type": "array",
            "items": {"type": "string"}
        },
        "license": {"type": "string"},
        "aiPreferences": {
            "type": "object",
            "required": ["styleGuide", "testingFramework", "promptOnMissing"],
            "properties": {
                "styleGuide": {"type": "string"},
                "testingFramework": {"type": "string"},
                "promptOnMissing": {"type": "boolean"}
            }
        }
    }
}

def ai_init(args):
    base = os.path.join(os.getcwd(), '.ai')
    os.makedirs(base, exist_ok=True)
    for d in DEFAULT_DIRS:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    config_path = os.path.join(base, '0-ai-config', 'ai-config.json')
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({
                "projectName": os.path.basename(os.getcwd()),
                "description": "",
                "primaryLanguage": "",
                "aiPreferences": {
                    "styleGuide": "",
                    "testingFramework": "",
                    "promptOnMissing": False
                }
            }, f, indent=2)
    context_path = os.path.join(base, '1-context', 'project_context.md')
    if not os.path.exists(context_path):
        with open(context_path, 'w') as f:
            f.write('# Project Context\n')
    print('Initialized .ai structure at', base)


def ai_migrate(args):
    readme = os.path.join(os.getcwd(), 'README.md')
    if not os.path.exists(readme):
        print('README.md not found', file=sys.stderr)
        return 1
    with open(readme) as f:
        lines = f.readlines()
    name = lines[0].strip('#\n ').strip() if lines else 'project'
    desc = ''
    for l in lines[1:5]:
        if l.strip():
            desc = l.strip()
            break
    base = os.path.join(os.getcwd(), '.ai')
    for d in DEFAULT_DIRS:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    config = {
        'projectName': name,
        'description': desc,
        'primaryLanguage': '',
        'aiPreferences': {
            'styleGuide': '',
            'testingFramework': '',
            'promptOnMissing': False
        }
    }
    with open(os.path.join(base, '0-ai-config', 'ai-config.json'), 'w') as f:
        json.dump(config, f, indent=2)
    with open(os.path.join(base, '1-context', 'project_context.md'), 'w') as f:
        f.write('# ' + name + '\n' + desc + '\n')
    print('Migrated README.md into .ai')


def _validate_schema(data, schema):
    """Very small subset of JSON schema validation used for tests."""
    if schema["type"] == "object":
        if not isinstance(data, dict):
            return False
        for key in schema.get("required", []):
            if key not in data:
                return False
        for key, subschema in schema.get("properties", {}).items():
            if key in data:
                if not _validate_schema(data[key], subschema):
                    return False
        return True
    if schema["type"] == "array":
        if not isinstance(data, list):
            return False
        item_schema = schema.get("items")
        if item_schema:
            for item in data:
                if not _validate_schema(item, item_schema):
                    return False
        return True
    if schema["type"] == "string":
        if not isinstance(data, str):
            return False
        if "minLength" in schema and len(data) < schema["minLength"]:
            return False
        return True
    if schema["type"] == "boolean":
        return isinstance(data, bool)
    return True

def ai_validate(args):
    base = os.path.join(os.getcwd(), '.ai')
    missing = []
    for d in DEFAULT_DIRS:
        if not os.path.isdir(os.path.join(base, d)):
            missing.append(d)
    config_path = os.path.join(base, '0-ai-config', 'ai-config.json')
    if not os.path.exists(config_path):
        missing.append('0-ai-config/ai-config.json')
        data = None
    else:
        with open(config_path) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print('Invalid JSON in ai-config.json', file=sys.stderr)
                return 1
    if missing:
        print('Missing required elements:', ', '.join(missing), file=sys.stderr)
        return 1
    if not _validate_schema(data, SCHEMA):
        print('ai-config.json does not match schema', file=sys.stderr)
        return 1
    print('Validation successful')
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog='ai-cli')
    sub = parser.add_subparsers(dest='command')
    sub.required = True

    p_init = sub.add_parser('ai-init', help='Initialize .ai directory structure')
    p_init.set_defaults(func=ai_init)

    p_mig = sub.add_parser('ai-migrate', help='Migrate README to .ai')
    p_mig.set_defaults(func=ai_migrate)

    p_val = sub.add_parser('ai-validate', help='Validate .ai structure')
    p_val.set_defaults(func=ai_validate)

    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == '__main__':
    sys.exit(main())
