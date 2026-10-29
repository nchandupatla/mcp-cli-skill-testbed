import os


def from_env(prefix="TINYCONF_"):
    return {k[len(prefix):].lower(): v for k, v in os.environ.items() if k.startswith(prefix)}
