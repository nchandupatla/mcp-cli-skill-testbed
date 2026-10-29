from tinyconf import parse_config


def test_parse_basic():
    assert parse_config("a = 1\nb = two")["b"] == "two"


def test_comments_skipped():
    assert "x" not in parse_config("# x = 1")
