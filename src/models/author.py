from sqlalchemy import Column, Integer, String

from .base_model import BaseModel


class Author(BaseModel):
  __tablename__ = 'authors'

  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
