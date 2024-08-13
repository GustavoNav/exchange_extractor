from sqlalchemy import create_engine

class DatabaseConnector:
    conn = None
    engine = None

    @classmethod
    def connect(cls):
        try:
            cls.engine = create_engine('postgresql://adm:adm321@postgres:5432/postgresDB')
        except Exception as exception:
            print("Database connection error: ", exception)