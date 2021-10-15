from sqlalchemy import Column, Integer, String, Boolean, text, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, server_default=text('0'))


def init_db(app):
    engine = create_engine(app.config["DATABASE"], echo=True)
    Base.metadata.create_all(engine)
    global_args()["engine"] = engine


def global_args(dt=dict()):
    return dt
