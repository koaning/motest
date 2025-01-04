# motest

Small cli that allows for more elaborate testing inside Marimo

## Installation

```bash
uv pip install motest
```

## Usage

Suppose that you have a notebook `some_notebook.py` that you want to test. Maybe with the following content:

```python
import marimo as mo
import pytest
return (mo,)

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,c", [(1, 1, 2), (1, 2, 3)])
def test_add(a, b, c):
    assert add(a, b) == c
```

You can test this notebook by running the following command:

```bash
python -m motest some_notebook.py
```

This is what the output will look like:

```
============================= test session starts ==============================
platform darwin -- Python 3.10.14, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/vincent/Development/motest
configfile: pyproject.toml
plugins: anyio-4.7.0
collected 2 items                                                              

test_some_notebook.py ..                                                   [100%]

============================== 2 passed in 0.11s ===============================
```

### How it works 

The setup is really minimal. We call the `marimo export script` command and write the Python code to a temporary file. We then point `pytest` to this file and do a cleanup after the tests are done. The status code is returned to the caller and you are also able to pass any `pytest` arguments to the command.
