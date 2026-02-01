# new_demo/tests/test_sample.py
import pytest

@pytest.mark.smoke
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.smoke
def test_subtraction():
    assert 5 - 3 == 2

def test_not_smoke():
    assert 10 * 2 == 20
