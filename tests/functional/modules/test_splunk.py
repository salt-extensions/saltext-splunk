import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("splunk.example_function"),
]


@pytest.fixture
def splunk(modules):
    return modules.splunk


def test_replace_this_this_with_something_meaningful(splunk):
    echo_str = "Echoed!"
    res = splunk.example_function(echo_str)
    assert res == echo_str
