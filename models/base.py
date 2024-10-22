from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from sqlalchemy.ext.declarative import declarative_base
from models.engine.database import session

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    
    def to_dict(self):
        """Converts a SQLAlchemy model instance to a dictionary."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def add(self):
        """Adds the current instance to the session."""
        session.add(self)
        session.commit()

    def update(self):
        """Commits the changes made to the current instance."""
        session.commit()

    def delete(self):
        """Deletes the current instance from the session."""
        session.delete(self)
        session.commit()
