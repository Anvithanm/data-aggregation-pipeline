# Variables
PYTHON := python
SRC_DIR := src
TEST_DIR := test
DATA_FILE := $(SRC_DIR)/1553768847-housing.csv
OUTPUT_FILE := $(SRC_DIR)/house_price_aggregates.json

# Phony targets
.PHONY: run test clean install help
# Targets

# Run the main program
run:
	@echo "Running the main program..."
	$(PYTHON) $(SRC_DIR)/main.py

# Run tests
test:
	@echo "Running unit tests..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "*.py"

# Clean generated files
clean:
	@echo "Cleaning up generated files..."
	rm -f $(OUTPUT_FILE)

# Install required dependencies
#Currently not used; requirements.txt is not created; For future use
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Help message
help:
	@echo "Makefile Usage:"
	@echo "  make run       - Run the main program"
	@echo "  make test      - Run unit tests"
	@echo "  make clean     - Remove generated output files"
	@echo "  make install   - Install required dependencies"
