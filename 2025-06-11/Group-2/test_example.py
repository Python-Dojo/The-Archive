from unittest.mock import patch

def foo():
    return 1

@patch("test_example.foo")
def test_bar(mock_foo):
    mock_foo.return_value = 2
    assert foo() == 2

def test_bar_2():
    with patch("test_example.foo") as mock_foo:
        mock_foo.return_value = 2
        print(foo(), "whattt")
        assert foo() in {1, 2}



test_bar_2()