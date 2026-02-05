import pytest

@pytest.mark.smoke
@pytest.mark.xray("COM-1")
def test_login():
    assert True


@pytest.mark.regression
@pytest.mark.xray("COM-2")
def test_profile():
    assert True
