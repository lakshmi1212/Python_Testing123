# Python Math Operations

This repository demonstrates basic math operations (addition and subtraction) with production-ready test automation using pytest and CI/CD workflow integration.

## Usage

- Business logic is in `src/math_operations.py`.
- Tests are in `tests/` folder.

## How to run tests locally

```bash
pip install -r default/requirements.txt
pytest tests/ -v --tb=short
```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Triggers on push to `.github/workflows` and pull requests to `main`.
- Runs tests using pytest.

## File Structure

- src/math_operations.py: Math functions
- tests/test_add.py: Addition tests
- tests/test_subtract.py: Subtraction tests
- default/requirements.txt: Python dependencies
- default/math.json: Metadata for workflow generation
