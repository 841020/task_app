from flask import jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean, text
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine('sqlite:///sample.db', echo=True)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, server_default=text('0'))


Base.metadata.create_all(engine)


def add_task(data):
    with Session(engine) as session:
        session.begin()
        try:
            new_task = Tasks(**data)
            session.add(new_task)
            session.flush()
        except:
            session.rollback()
            raise
        else:
            return str(new_task.id)
        finally:
            session.commit()


def get_tasks_list():
    with Session(engine) as session:
        session.begin()
        try:
            rows = session.query(Tasks).all()
            result = []
            for row in rows:
                row.__dict__.pop('_sa_instance_state')
                result.append(row.__dict__)
        except:
            session.rollback()
            raise
        else:
            return jsonify({'result': result})
        finally:
            session.commit()


def get_task(data_id):
    with Session(engine) as session:
        session.begin()
        try:
            row = session.query(Tasks).get(data_id)
            row.__dict__.pop('_sa_instance_state')
        except:
            session.rollback()
            raise
        else:
            return jsonify({'result': row.__dict__})
        finally:
            session.commit()
