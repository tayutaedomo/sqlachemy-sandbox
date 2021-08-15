from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from .base_model import BaseModel


class Comment(BaseModel):
  __tablename__ = 'comments'

  id = Column(Integer, primary_key=True)
  subject = Column(String(255), nullable=False)
  text = Column(Text, nullable=False)

  book_id = Column(
      INTEGER(11),
      ForeignKey('books.id', ondelete='restrict', onupdate='cascade'),
      nullable=True,
      index=True,
      unique=False
  )
  book = relationship('books')
