from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()
engine = create_engine('sqlite:////sample.db', echo=True)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean)


Base.metadata.create_all(engine)


def get_tasks_list():
    with Session(engine) as session:
        return session.query(Tasks).all()
