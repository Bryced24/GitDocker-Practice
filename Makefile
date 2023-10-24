# Makefile

.PHONY: all
all: local-unit-test local-kattis-test style-check fix-style type-check

.PHONY: run
run:
	python hvert.py

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf hvertskalmaeta/*.pyc  # Clean any compiled files in your hvertskalmaeta folder

# a. Rule for local unit test
.PHONY: local-unit-test
local-unit-test:
	pytest --verbose test_nearest_city.py

# b. Rule for local Kattis test on sample input/output files
.PHONY: local-kattis-test
local-kattis-test:
	@for i in 1 2; do \
		cat samples/$$i.in | python hvert.py | diff - samples/$$i.ans; \
	done
	@echo "Local Kattis tests passed..."

# c. Rule for checking styles using flake8
.PHONY: style-check
style-check:
	flake8 .

# d. Rule for fixing styles using autopep8
.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

# e. Rule for checking types with mypy
.PHONY: type-check
type-check:
	mypy --strict .

# f. Rule to submit problem to Kattis using Kattis CLI
.PHONY: submit-kattis
submit-kattis:
	kattis -f hvert.py -p hvertskalmaeta
