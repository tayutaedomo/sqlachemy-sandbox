from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from .base_model import BaseModel


class Book(BaseModel):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
  description = Column(Text)

  # author_id = Column(
  #     Integer,
  #     ForeignKey('authors.id'),
  #     nullable=False,
  #     index=True,
  #     unique=False
  # )
  # author = relationship('Author')
