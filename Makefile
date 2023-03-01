# This is a Makefile that defines the following targets:
# 	1. A "build" command that makes a python wheel for the llmfyi module.
# 	2. A "doc" command that rebuilds documentation
# 	3. A "test" command that runs pytest
# 	4. A default command that does everything

.PHONY: build doc test

build:
	python setup.py bdist_wheel

doc:
	cd docs && make html

test:
	pytest

publish:
	pip-compile

default: build doc test

