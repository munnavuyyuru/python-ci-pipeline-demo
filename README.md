<div align="center"> 
  <h1>Python CI Pipeline Demo</h1> 
  <p> 
    <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python Version"> </a> 
    <a href="https://github.com/psf/black"> <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"> </a> 
    <a href="https://github.com/PyCQA/pylint"> <img src="https://img.shields.io/badge/linting-pylint-yellowgreen" alt="Linting: pylint"> </a> 
    <a href="https://github.com/PyCQA/bandit"> <img src="https://img.shields.io/badge/security-bandit-yellow.svg" alt="Security: bandit"> </a> 
    <a href="https://github.com/pre-commit/pre-commit"> <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="Pre-commit"> </a> </p> 
</div>

> Production-grade CI/CD pipeline demonstration with comprehensive testing, linting, and security scanning.

## 📋 Features

- ✅ **100% Test Coverage** - Comprehensive test suite with 87+ tests
- 🔍 **Multiple Linting Tools** - Black, Flake8, Pylint, isort
- 🔒 **Security Scanning** - Bandit for security vulnerabilities
- 📊 **Type Checking** - MyPy for static type analysis
- 🚀 **CI/CD Ready** - GitHub Actions workflow (coming soon)
- 📦 **Clean Architecture** - Well-organized project structure


## 📁 Project Structure

```text
python-ci-pipeline-demo/
├── src/                  # Source code
│   ├── calculator.py     # Calculator implementation
│   └── utils.py          # Utility functions
│
├── tests/                # Test suite
│   ├── test_calculator.py  # Calculator tests
│   └── test_utils.py       # Utility tests
│
├── scripts/              # Helper scripts
│   ├── lint.sh           # Run all linting checks
│   └── format.sh         # Auto-format code
│
├── .github/              # GitHub Actions (coming soon)
│
└── pyproject.toml        # Project configuration
```


## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/munnavuyyuru/python-ci-pipeline-demo.git
cd python-ci-pipeline-demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# View coverage report

# On Mac
open htmlcov/index.html

# On Linux
xdg-open htmlcov/index.html
```

## 🔍 Code Quality Checks

```bash
# Run all linting checks
./scripts/lint.sh

# Auto-format code
./scripts/format.sh

# Individual tools
black src/ tests/          # Format code
flake8 src/ tests/         # Style check
pylint src/                # Code analysis
mypy src/                  # Type check
bandit -r src/             # Security scan
```
## 📊 Code Quality Metrics

* **Test Coverage:** 100%
* **Pylint Score:** 9.85/10
* **Security Issues:** 0
* **Code Style:** Black compliant

---

## 🛠️ Tools Used

| Tool       | Purpose                           |
| ---------- | --------------------------------- |
| pytest     | Testing framework                 |
| pytest-cov | Coverage reporting                |
| black      | Code formatting                   |
| isort      | Import sorting                    |
| flake8     | Style guide enforcement           |
| pylint     | Code analysis                     |
| mypy       | Static type checking              |
| bandit     | Security linting                  |
| safety     | Dependency vulnerability checking |

---

## 📝 Usage Example

```python id="py001"
from src.calculator import Calculator

# Create calculator instance
calc = Calculator()

# Perform calculations
result = calc.add(10, 5)        # 15.0
result = calc.multiply(3, 4)    # 12.0
result = calc.power(2, 8)       # 256.0

# View history
history = calc.get_history()
```
## 📄 License
This project is licensed under the **MIT License** – see the `LICENSE` file for details.

## Acknowledgments
This project was built as a production-grade demonstration of CI/CD pipelines for DevOps/DevSecOps learning.
