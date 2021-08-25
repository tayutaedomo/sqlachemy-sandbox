import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.db import get_session  # noqa: F401, E402 isort:skip
from models import Book  # noqa: F401, E402 isort:skip
from tests.factories import AuthorFactory, BookFactory  # noqa: F401, E402 isort:skip


def test_01():
  session = get_session()

  authtor = AuthorFactory()
  session.flush()

  BookFactory(author_id=authtor.id)

  books = session.query(Book).all()

  assert books is not None
  print(books[0].name, books[0].description)


def test_02():
  assert not False
