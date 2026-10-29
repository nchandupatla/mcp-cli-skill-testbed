DEFAULT_TIMEOUT = 30


def parse_config(text):
    """Parse simple `key = value` lines into a dict."""
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip()
    out.setdefault("timeout", DEFAULT_TIMEOUT)
    return out
