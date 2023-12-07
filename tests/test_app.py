from python_skeleton.app import say_hello_to


def test_say_hello_to():
    actual = say_hello_to("foo")
    assert actual == "Hello foo!"
