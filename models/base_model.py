from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin, SerializeMixin, SmartQueryMixin

Base: DeclarativeMeta = declarative_base()


class BaseModel(ActiveRecordMixin, SmartQueryMixin, ReprMixin, SerializeMixin):
  __abstract__ = True
