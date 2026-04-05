#!/bin/bash

set -e

echo " Auto-fixing code formatting     "
echo "---------------------------------"


# Color codes
GREEN='\033[0;32m'
NC='\033[0m'

echo "Running Black (formatter)..."
black src/ tests/
echo -e "${GREEN}✓ Black complete${NC}"
echo ""

echo "Running isort (import sorter)..."
isort src/ tests/
echo -e "${GREEN}✓ isort complete${NC}"
echo ""

echo "----------------------------------"
echo -e "${GREEN}✓ Auto-formatting complete!${NC}"
echo ""
