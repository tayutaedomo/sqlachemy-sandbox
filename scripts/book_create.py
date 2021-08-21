import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.db import has_session, create_engine, setup_db, get_session  # noqa: F401, E402 isort:skip
from models import Book  # noqa: F401, E402 isort:skip

DB_NAME = os.environ.get('DB_NAME', 'mydb')


if __name__ == "__main__":
  if not has_session():
    try:
      options = {
          'echo': True
      }
      engine = create_engine(db_name=DB_NAME, options=options)
      setup_db(engine)
    except Exception as e:
      raise e

  try:
    session = get_session()

    # book = Book(name='Book A', description='Book A desc')
    # session.add(book)
    Book(name='Book A', description='Book A desc')

    session.commit()
  except Exception as e:
    raise e
  finally:
    get_session().remove()
