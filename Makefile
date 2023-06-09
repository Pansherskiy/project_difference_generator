install:
	poetry install

update:
	poetry update

reinstall:
	pip install --user --force-reinstall dist/*.whl

simple_gendiff:
	poetry run gendiff tests/fixtures/json_file1.json tests/fixtures/json_file2.json

nested_gendiff:
	poetry run gendiff tests/fixtures/nested_json_file1.json tests/fixtures/nested_json_file2.json

help:
	poetry run gendiff -h

build:
	poetry build

check:
	poetry check

coverage:
	poetry run pytest --cov=gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 .

test:
	poetry run pytest -vv --color=yes --exitfirst tests

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
