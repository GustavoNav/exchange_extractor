from sqlalchemy import create_engine

class DatabaseConnector:
    conn = None
    engine = None

    @classmethod
    def connect(cls):
        try:
            cls.engine = create_engine('postgresql://adm:adm321@localhost:5455/postgresDB')
            cls.conn = cls.engine.connect()
            return cls.conn
        
        except Exception as exception:
            print("Database connection error: ", exception)