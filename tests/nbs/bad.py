import marimo

__generated_with = "0.10.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    def add(a, b):
        return a + b
    return (add,)


@app.cell
def _(add):
    import pytest

    @pytest.mark.parametrize("a,b,c", [(1, 1, 2), (1, 2, 5)])
    def test_add(a, b, c):
        assert add(a, b) == c
    return pytest, test_add


if __name__ == "__main__":
    app.run()
