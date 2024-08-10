import pandas as pd
from sqlalchemy import create_engine, MetaData

class DatabaseConnector:
    engine = None
    connection = None
    metadata = None

    @classmethod
    def connect(cls):
        try:
            cls.engine = create_engine('postgresql://adm:adm321@localhost:5455/postgresDB')
            cls.connection = cls.engine.connect()
            cls.metadata = MetaData()  
            cls.metadata.reflect(bind=cls.engine)

        except Exception as exception:
            print("Database connection error: ", exception)