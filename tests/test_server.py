from tinyconf.core import parse_config


def test_port_parsed():
    assert parse_config("port = 9000")["port"] == "9000"
