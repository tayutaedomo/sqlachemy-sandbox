from sqlalchemy import Column, Integer, String, Text

from .base_model import BaseModel


class Book(BaseModel):
  __table__ = 'books'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  description = Column(Text)
