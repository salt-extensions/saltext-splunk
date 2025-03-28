"""
:codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from saltext.splunk.states import splunk_search


@pytest.fixture
def configure_loader_modules():
    return {splunk_search: {}}


def test_present():
    """
    Test to ensure a search is present.
    """
    name = "API Error Search"

    ret = {"name": name, "changes": {}, "result": None, "comment": ""}

    mock = MagicMock(side_effect=[True, False, False, True])
    with patch.dict(
        splunk_search.__salt__,
        {"splunk_search.get": mock, "splunk_search.create": mock},
    ):
        with patch.dict(splunk_search.__opts__, {"test": True}):
            comt = f"Would update {name}"
            ret.update({"comment": comt})
            assert splunk_search.present(name) == ret

            comt = f"Would create {name}"
            ret.update({"comment": comt})
            assert splunk_search.present(name) == ret

        with patch.dict(splunk_search.__opts__, {"test": False}):
            ret.update({"comment": "", "result": True, "changes": {"new": {}, "old": False}})
            assert splunk_search.present(name) == ret


def test_absent():
    """
    Test to ensure a search is absent.
    """
    name = "API Error Search"

    ret = {"name": name, "result": None, "comment": ""}

    mock = MagicMock(side_effect=[True, False])
    with patch.dict(splunk_search.__salt__, {"splunk_search.get": mock}):
        with patch.dict(splunk_search.__opts__, {"test": True}):
            comt = f"Would delete {name}"
            ret.update({"comment": comt})
            assert splunk_search.absent(name) == ret

        comt = f"{name} is absent."
        ret.update({"comment": comt, "result": True, "changes": {}})
        assert splunk_search.absent(name) == ret
