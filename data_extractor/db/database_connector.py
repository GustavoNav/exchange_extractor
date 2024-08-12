from sqlalchemy import create_engine

class DatabaseConnector:
    engine = None
    conn = None

    @classmethod
    def connect(cls):
        try:
            cls.engine = create_engine('postgresql://adm:adm321@postgres:5432/postgresDB')
            cls.conn = cls.engine.connect()
            return cls.conn

        except Exception as exception:
            print("Database connection error: ", exception)