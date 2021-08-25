import os
import sys

import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models import Comment  # noqa: F401, E402 isort:skip


class CommentFactory(Factory):
  class Meta:
    model = Comment
    sqlalchemy_session = Comment.session
    sqlalchemy_session_persistence = 'flush'

  subject = factory.Sequence(lambda n: f'Comment subject {n}')
  text = factory.Sequence(lambda n: f'Text {n}')
