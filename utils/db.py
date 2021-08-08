import os

from typing import Optional, Union

from sqlalchemy import create_engine as create_engine_
from sqlalchemy.engine import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import BaseModel


DB_NAME = os.environ.get('DB_NAME', 'mydb')

DEFAULT_QUERY_ENGINE_URL = {'charset': 'utf8'}

session: Optional[scoped_session] = None


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
