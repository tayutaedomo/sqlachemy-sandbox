import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(ROOT_PATH)

from utils.db import get_session
from models.book import Book
from tests.factories.book_factory import BookFactory


def test_01():
  session = get_session()

  BookFactory()

  books = session.query(Book).all()

  assert books is not None
  print(books[0].name, books[0].description)


def test_02():
  assert not False
