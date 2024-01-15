import pytest

pytestmark = [
    pytest.mark.requires_salt_states("splunk.exampled"),
]


@pytest.fixture
def splunk(states):
    return states.splunk


def test_replace_this_this_with_something_meaningful(splunk):
    echo_str = "Echoed!"
    ret = splunk.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
