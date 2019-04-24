from sqlalchemy import create_engine
from ..settings import config

class DB_Connection:
    def __init__(self, host=None, port=None, username=None, password=None, db_name=None):
        self.host = host if host else config.DB_HOST
        self.port = port if port else config.DB_PORT
        self.username = username if username else config.DB_USER
        self.password = password if password else config.DB_PASSWORD
        self.dbs = db_name if db_name else config.DB_NAME

    def get_engine(self):
        print(self.dbs)
        return create_engine('mysql+mysqldb://{username}:{password}@{host}:{port}/{dbs}'.format(
            username=self.username, password=self.password, host=self.host, port=self.port, dbs=self.dbs))
