from .database_connector import DatabaseConnector

'''test database connector'''
def test_connect_01():
    conn = DatabaseConnector.connect()