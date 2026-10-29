from tinyconf.yaml_loader import parse_yaml


def test_yaml_two_keys():
    cfg = parse_yaml("host: example.com\nport: 9000")
    assert cfg["port"] == "9000"
