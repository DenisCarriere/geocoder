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
	make -C docs html
	xdg-open docs/_build/html/index.html