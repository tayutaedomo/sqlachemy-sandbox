import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.db import has_session, create_engine, setup_db, get_session  # noqa: F401, E402 isort:skip


DB_NAME = os.environ.get('DB_NAME', 'mytestdb')


def pytest_configure(config):
  if not has_session():
    try:
      options = {
          'echo': True
      }
      engine = create_engine(db_name=DB_NAME, options=options)
      setup_db(engine)
      print('\nDB initialzed.\n')
    except Exception as e:
      raise e


def pytest_runtest_setup(item: pytest.Item) -> None:
  pass


@pytest.fixture(scope='session', autouse=True)
def scope_session():
  yield
  get_session().close()
  print('\n\nDB session closed.')


@pytest.fixture(scope='module', autouse=True)
def scope_module():
  yield


@pytest.fixture(scope='class', autouse=True)
def scope_class():
  yield


@pytest.fixture(scope='function', autouse=True)
def scope_function():
  yield
  get_session().rollback()
