from .database_connector import DatabaseConnector
import pandas as pd
from sqlalchemy import create_engine, select, text

# def test_connect_01():
#     conn = DatabaseConnector.connect()

def test_select_01():
    conn = DatabaseConnector.connect()

    result = conn.execute(text("select * from tb_historico"))
    print(result.all())



