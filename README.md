# Calculator Project

A small Python module providing two arithmetic functions:

| Function | Behavior |
| --- | --- |
| `add(a, b)` | Returns `a + b`. |
| `sub(a, b)` | Returns `a - b` (the order of the operands matters). |

The implementation is in `Calculator.py`. It uses Python's arithmetic
operators directly, with no input validation or external dependencies.
It supports integers and floating-point numbers, including negative values.
Unsupported operand combinations raise Python's normal `TypeError`.

## Usage

Install Python 3 and run Python from the repository directory:

```python
from Calculator import add, sub

print(add(5, 3))  # 8
print(sub(5, 3))  # 2
```

This project is an importable module, not an interactive calculator.
Running `python Calculator.py` defines the functions but produces no output.

## Tests

The tests use Python's built-in `unittest` framework; no packages need to be
installed. From the repository directory, run:

```sh
python -m unittest discover -s tests -v
```

The suite covers addition and subtraction with positive and negative operands,
zero, equal operands, floating-point and mixed numeric inputs, large integers,
and unsupported operand combinations.

## Continuous integration

`.github/workflows/tests.yml` runs the same test command with Python 3.13 on
GitHub Actions for every push to any branch and for pull requests. There are no
branch or path filters.
