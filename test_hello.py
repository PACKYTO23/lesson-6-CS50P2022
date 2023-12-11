from hello import hello


def test_default():
    assert hello() == "Hello, World!"


def test_argument():
    assert hello("Juan") == "Hello, Juan!"


def test_list():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}!"
