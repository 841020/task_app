from flask import jsonify
from sqlalchemy.orm import Session

from models import engine


def create_row(table, data):
    with Session(engine) as session:
        session.begin()
        try:
            new_row = table(**data)
            session.add(new_row)
            session.flush()
        except:
            session.rollback()
            raise
        else:
            return str(new_row.id)
        finally:
            session.commit()


def read_rows_list(table):
    with Session(engine) as session:
        session.begin()
        try:
            rows = session.query(table).all()
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


def read_row(table, row_id):
    with Session(engine) as session:
        session.begin()
        try:
            row = session.query(table).get(row_id)
            row.__dict__.pop('_sa_instance_state')
        except:
            session.rollback()
            raise
        else:
            return jsonify({'result': row.__dict__})
        finally:
            session.commit()


def update_row(table, row_id, data):
    with Session(engine) as session:
        session.begin()
        try:
            session.query(table).filter_by(id=row_id).update(data)
        except:
            session.rollback()
            raise
        finally:
            session.commit()


def delete_row(table, row_id):
    with Session(engine) as session:
        session.begin()
        try:
            session.query(table).filter_by(id=row_id).delete()
        except:
            session.rollback()
            raise
        finally:
            session.commit()
