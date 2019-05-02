from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from ..settings import config
from contextlib import contextmanager

class DB_Connection:
    def __init__(self, host=None, port=None, username=None, password=None, db_name=None):
        self.host = host if host else config.DB_HOST
        self.port = port if port else config.DB_PORT
        self.username = username if username else config.DB_USER
        self.password = password if password else config.DB_PASSWORD
        self.dbs = db_name if db_name else config.DB_NAME

        self.engine = self.get_engine()

    def get_engine(self):
        print(self.dbs)
        return create_engine('mysql+pymysql://{username}:{password}@{host}:{port}/{dbs}'.format(
            username=self.username, password=self.password, host=self.host, port=self.port, dbs=self.dbs))

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session


Session = DB_Connection().get_session()

@contextmanager
def open_session():
    """
    可以使用 with 上下文，在 with 结束之后自动 commit
    """
    _session = Session()
    try:
        yield _session
        _session.commit()
    except Exception as e:
        # _session.rollback()
        raise e
    finally:
        _session.close()


def excute_query(sql, params=None):
    with open_session() as session:
        try:
            result = session.excute(text(sql), params).fetchall()
        except Exception as e:
            session.rollback()
        else:
            return result


def excute_update(sql, params):
    with open_session() as session:
        try:
            session.excute(text(sql), params)
            print("excuted")
        except Exception as e:
            session.rollback()
        else:
            return True


def excute_delete(sql, params):
    with open_session() as session:
        try:
            session.excute(text(sql), params)
        except Exception as e:
            session.rollback()
        else:
            return True


