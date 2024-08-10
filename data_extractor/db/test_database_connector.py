from .database_connector import DatabaseConnector
from sqlalchemy import text

'''Test connection with postgres'''
def test_connect_01():
    conn = DatabaseConnector.connect()

    result = conn.execute(text("select * from tb_historico"))
    print(result.all())



