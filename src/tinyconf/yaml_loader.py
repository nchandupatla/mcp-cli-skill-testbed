from .core import parse_config


def parse_yaml(text):
    """Very small YAML subset: `key: value` lines."""
    return parse_config(text.replace(":", "=", 1))
