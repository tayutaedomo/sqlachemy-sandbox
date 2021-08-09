import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(ROOT_PATH)

from typing import Optional, Union

from sqlalchemy import create_engine as create_engine_
from sqlalchemy.engine import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import BaseModel

DEFAULT_QUERY_ENGINE_URL = {'charset': 'utf8'}

session: Optional[scoped_session] = None

DB_NAME = os.environ.get('DB_NAME', 'mydb')


def create_engine(
    db_name: Optional[str] = None,
    user: str = 'root',
    password: str = 'root',
    host: str = '127.0.0.1',
    port: Union[int, str] = 3306,
    options: Optional[dict] = None,
) -> Engine:
  query = {**DEFAULT_QUERY_ENGINE_URL}

  url = URL(
      drivername='mysql+pymysql',
      database=db_name,
      username=user,
      password=password,
      host=host,
      port=port,
      query=query
  )

  opts = {**(options if options is not None else {})}

  print(url)
  print(opts)
  return create_engine_(url, **opts)


def setup_db(engine: Engine) -> scoped_session:
  _session = scoped_session(sessionmaker(engine))

  BaseModel.set_session(_session)

  global session
  session = _session

  return _session


def get_session() -> scoped_session:
  global session

  if session is None:
    raise Exception('You must call setup_db()!')

  return session


def has_session() -> bool:
  global session
  return session is not None


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
    pass
  except Exception as e:
    raise e
  finally:
    get_session().remove()
