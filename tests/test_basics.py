from pathlib import Path

from motest import motest

def test_good_notebook():
    assert motest(Path("tests/nbs/good.py")) == 0

def test_bad_notebook():
    assert motest(Path("tests/nbs/bad.py")) == 1
