# tinyconf

A tiny config loader. This repo is a **test bed** for the "MCP vs CLI vs Skills" experiment: AI agents read and write here on purpose. Issues and pull requests may be opened and closed by test runs.

## Usage

```python
from tinyconf import parse_config
parse_config("timeout = 10")
```

## Testing

Run `PYTHONPATH=src pytest -q` to run the tests.

