import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(ROOT_PATH)

from utils.db import has_session, create_engine, setup_db, get_session
from models.book import Book

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

    book = (
        session.query(Book)
        .one_or_none()
    )

    if book is not None:
      book.name = book.name + ' updated'

    session.commit()
  except Exception as e:
    raise e
  finally:
    get_session().remove()
