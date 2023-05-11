
# flake8: noqa F403

import pytest

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')


@pytest.fixture(scope='session')
def browser_config(request):
    return request.config.getoption('--browser')
