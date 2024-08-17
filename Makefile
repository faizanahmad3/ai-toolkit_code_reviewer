.PHONY: style lint

# Format Python code with isort and black
style:
	@echo "Formatting Python code with isort and black..."; \
	isort .; \
	black .

# Lint Python code with flake8
lint:
	@echo "Linting Python code with flake8..."; \
	flake8 .
