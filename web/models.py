import json

from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session


Base = declarative_base()
engine = create_engine('sqlite:///sample.db', echo=True)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, server_default=text('0'))


Base.metadata.create_all(engine)


def get_tasks_list():
    result = []
    with Session(engine) as session:
        session.begin()
        try:
            rows = session.query(Tasks).all()
            result = []
            for row in rows:
                row.__dict__.pop('_sa_instance_state')
                result.append(row.__dict__)
            output = json.dumps({'result': result})
        except:
            session.rollback()
            raise
        else:
            session.commit()
    return output


def add_task(data):
    with Session(engine) as session:
        session.begin()
        try:
            new_task = Tasks(**data)
            session.add(new_task)
        except:
            session.rollback()
            raise
        else:
            session.commit()


def get_task(data):
    result = []
    with Session(engine) as session:
        session.begin()
        try:
            rows = session.query(Tasks).filter_by(**data).all()
            result = []
            for row in rows:
                row.__dict__.pop('_sa_instance_state')
                result.append(row.__dict__)
            output = json.dumps({'result': result})
        except:
            session.rollback()
            raise
        else:
            session.commit()
    return output
