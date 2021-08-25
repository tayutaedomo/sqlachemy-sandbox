import os
import sys

import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models import Book, Author  # noqa: F401, E402 isort:skip
from .author_factory import AuthorFactory  # noqa: F401, E402 isort:skip


class BookFactory(Factory):
  class Meta:
    model = Book
    sqlalchemy_session = Book.session
    sqlalchemy_session_persistence = 'flush'

  name = factory.Sequence(lambda n: f'Book name {n}')
  description = factory.Sequence(lambda n: f'Description {n}')

  # author = factory.SubFactory(AuthorFactory)
