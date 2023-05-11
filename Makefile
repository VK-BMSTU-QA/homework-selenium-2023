run-linter:
	flake8 hw/code/*/*.py

run-tests:
	bash runner_tests.sh

show-results-allure:
	allure serve /allure-results

set-env:
	set -a && source .env && set +a

