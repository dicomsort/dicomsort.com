.PHONY: build dev test clean install help

# Default target
help:
	@echo "Available targets:"
	@echo "  install    - Install Python dependencies"
	@echo "  dev        - Run development server"
	@echo "  build      - Build static site for production"
	@echo "  test       - Test the development version"
	@echo "  clean      - Clean build artifacts"
	@echo "  help       - Show this help message"

# Install dependencies
install:
	pip install -r requirements.txt

# Run development server
dev:
	FLASK_ENV=development python -m flask run --host=0.0.0.0 --port=5000

# Build static site using frozen-flask
build: install
	FLASK_ENV=production python setup.py freeze
	@echo "Static site built in build/ directory

# Test development version
test: install
	@echo "Testing development server..."
	FLASK_ENV=development python -c "from app import app; app.test_client().get('/')"
	@echo "Development version test passed"

# Clean build artifacts
clean:
	rm -rf build/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
