#!/bin/bash

# This script runs multiple code quality checks on a Python project.
# It stops immediately if any unexpected error occurs.

set -e  # Exit on error

echo "Starting code quality checks..."
echo "--------------------------------"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'


OVERALL_STATUS=0

# Function to run a check and track status
run_check() {
    local name=$1
    local command=$2

    echo "Running $name..."
    if eval "$command"; then
        echo -e "${GREEN}✓ $name passed${NC}"
    else
        echo -e "${RED}✗ $name failed${NC}"
        OVERALL_STATUS=1
    fi
    echo ""
}

# Black - Code formatting check
run_check "Black (Code Formatting)" "black --check src/ tests/"

# isort - Import sorting check
run_check "isort (Import Sorting)" "isort --check-only src/ tests/"

# Flake8 - Style guide enforcement
run_check "Flake8 (Style Guide)" "flake8 src/ tests/"

# Pylint - Code analysis
run_check "Pylint (Code Analysis)" "pylint src/"

# MyPy - Type checking
run_check "MyPy (Type Checking)" "mypy src/"

# Bandit - Security issues
run_check "Bandit (Security Scan)" "bandit -r src/ -c .bandit"

# Safety - Dependency vulnerabilities
run_check "Safety (Dependency Check)" "safety scan --json || true"


echo "=================================="
if [ $OVERALL_STATUS -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
else
    echo -e "${RED}❌ Some checks failed. Please fix the issues above.${NC}"
fi

exit $OVERALL_STATUS
