# Python Math Operations

This repository contains simple Python functions for addition and subtraction, along with comprehensive tests and CI workflow guidance.

## Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)         # 5
result_subtract = subtract(5, 2)  # 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
python -m pytest tests/ -v --tb=short
```

## CI Workflow

The repository is designed for GitHub Actions CI using the workflow file at `.github/workflows/ci.yml`.

- Python version: 3.10
- Test command: `python -m pytest tests/ -v --tb=short`
- Dependencies: See `default/requirements.txt`

---
