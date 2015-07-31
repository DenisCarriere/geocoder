.PHONY: docs

setup:
	python setup.py install

init:
	pip install -r requirements.txt

test:
	py.test test_geocoder.py --verbose

clean:
	python setup.py clean --all
	rm -rf build-*
	rm -rf *egg*
	rm -rf dist

tox:
	tox

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload

register:
	python setup.py register

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"