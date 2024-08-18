from .database_connector import DatabaseConnector
from sqlalchemy import text
import pandas as pd
import os

class DatabaseRepository:

    @classmethod
    def select_historic(cls, company_codes):
        conn = DatabaseConnector.connect()

        if not isinstance(company_codes, list) or not company_codes:
            raise ValueError("company_codes deve ser uma lista não vazia de códigos.")

        company_codes_tuple = tuple(company_codes)

        with conn.begin():
            result = conn.execute(text(
                '''SELECT * FROM tb_historic
                   WHERE company_code IN :company_codes'''
            ), {'company_codes': company_codes_tuple})

        base_path = os.path.dirname(os.path.abspath(__file__))  
        parquet_file_path = os.path.join(base_path, '..', 'export', 'historic.parquet')
        
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
         
        df.to_parquet(parquet_file_path, index=False)

    @classmethod
    def select_general_financials(cls, company_codes):
        conn = DatabaseConnector.connect()

        if not isinstance(company_codes, list) or not company_codes:
            raise ValueError("company_codes deve ser uma lista não vazia de códigos.")

        company_codes_tuple = tuple(company_codes)

        with conn.begin():
            result = conn.execute(text(
                '''SELECT * FROM tb_general_financials
                   WHERE company_code IN :company_codes'''
            ), {'company_codes': company_codes_tuple})

        base_path = os.path.dirname(os.path.abspath(__file__))
        parquet_file_path = os.path.join(base_path, '..', 'export', 'general_financials.parquet')  

        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        
        print(df)

        df.to_parquet(parquet_file_path, index=False)

    @classmethod
    def select_real_time(cls, company_codes):
        conn = DatabaseConnector.connect()

        if not isinstance(company_codes, list) or not company_codes:
            raise ValueError("company_codes deve ser uma lista não vazia de códigos.")

        company_codes_tuple = tuple(company_codes)

        with conn.begin():
            result = conn.execute(text(
                '''SELECT * FROM tb_real_time
                   WHERE company_code IN :company_codes'''
            ), {'company_codes': company_codes_tuple})

        base_path = os.path.dirname(os.path.abspath(__file__))
        parquet_file_path = os.path.join(base_path, '..', 'export', 'real_time.parquet')  

        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        
        df.to_parquet(parquet_file_path, index=False)