.PHONY: docs

setup:
	python setup.py install

init:
	pip install -r requirements.txt

test:
	py.test -n auto tests --doctest-modules --pep8 geocoder -v --cov geocoder --cov-report term-missing

clean:
	python setup.py clean --all
	rm -rf build-*
	rm -rf *egg*
	rm -rf dist

tox:
	tox

publish:
	pandoc --from=markdown --to=rst --output README.rst README.md
	python setup.py sdist upload
	python setup.py bdist_wheel upload

register:
	pandoc --from=markdown --to=rst --output README.rst README.md
	python setup.py register

docs:
	make -C docs html
	xdg-open docs/_build/html/index.html
