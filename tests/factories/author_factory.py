import os
import sys

import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models import Author  # noqa: F401, E402 isort:skip


class AuthorFactory(Factory):
  class Meta:
    model = Author
    sqlalchemy_session = Author.session
    sqlalchemy_session_persistence = 'flush'

  name = factory.Sequence(lambda n: f'Author name {n}')
