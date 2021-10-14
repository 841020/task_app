
from sqlalchemy import create_engine, Column, Integer, String, Boolean, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///sample.db', echo=True)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, server_default=text('0'))


Base.metadata.create_all(engine)
