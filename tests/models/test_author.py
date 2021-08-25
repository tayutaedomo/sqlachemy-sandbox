import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.db import get_session  # noqa: F401, E402 isort:skip
from models import Author  # noqa: F401, E402 isort:skip
from tests.factories import AuthorFactory  # noqa: F401, E402 isort:skip


def test_01():
  session = get_session()

  AuthorFactory()

  session.commit()

  authors = session.query(Author).all()

  assert len(authors) == 1
  print(authors)
