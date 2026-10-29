from .core import parse_config


def load_server_settings(path):
    with open(path) as f:
        cfg = parse_config(f.read())
    return {"host": cfg.get("host", "localhost"), "port": int(cfg.get("port", 8080))}
