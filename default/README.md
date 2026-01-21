# Python Math Operations

This repository provides basic math operations (addition and subtraction) with production-ready test coverage and CI integration.

## Structure
- `src/math_operations.py`: Core math functions
- `tests/test_add.py`: Pytest cases for addition
- `tests/test_subtract.py`: Pytest cases for subtraction
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow metadata

## Usage
```python
from src.math_operations import add, subtract
print(add(2, 3))       # 5
print(subtract(2, 3))  # -1
```

## Running Tests
```sh
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow
- Automated workflow defined in `.github/workflows/ci.yml`
- See `default/math.json` for workflow metadata
