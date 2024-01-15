import pytest
import salt.modules.test as testmod
import saltext.splunk.modules.splunk_mod as splunk_module
import saltext.splunk.states.splunk_mod as splunk_state


@pytest.fixture
def configure_loader_modules():
    return {
        splunk_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        splunk_state: {
            "__salt__": {
                "splunk.example_function": splunk_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'splunk.example_function' returned: '{echo_str}'",
    }
    assert splunk_state.exampled(echo_str) == expected
