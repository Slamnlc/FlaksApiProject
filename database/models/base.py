from flask_sqlalchemy.query import Query


class Base:
    query: Query

    def __init__(self, *args, **kwargs):
        pass

    @property
    def session(self):
        return self.query.session

    def commit(self):
        return self.session.commit()

    def add(self):
        self.session.add(self)
        self.commit()

    @classmethod
    def exists(cls, **kwargs) -> bool:
        query = cls.query.filter_by(**kwargs).exists()
        return cls.query.session.query(query).scalar()

    @classmethod
    def filter_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs)
