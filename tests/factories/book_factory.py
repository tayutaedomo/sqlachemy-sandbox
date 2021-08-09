import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(ROOT_PATH)

import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory

from models.book import Book


class BookFactory(Factory):
  class Meta:
    model = Book
    sqlalchemy_session = Book.session
    sqlalchemy_session_persistence = 'flush'

  name = factory.Sequence(lambda n: f'name {n}')
  description = factory.Sequence(lambda n: f'description {n}')
