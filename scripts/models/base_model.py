from sqlalchemy.ext.declarative import DeclarativeMeta, declartive_base
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin, SerializeMixin, SmartQueryMixin

Base: DeclarativeMeta = declartive_base()


class BaseModel(ActiveRecordMixin, SmartQueryMixin, ReprMixin, SerializeMixin):
  __abstract__ = True
