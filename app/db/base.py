from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.inspection import inspect

@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
