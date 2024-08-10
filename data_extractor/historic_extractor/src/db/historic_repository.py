from data_extractor.db.database_connector import DatabaseConnector
from sqlalchemy import create_engine, Table, MetaData

class HistoricRepository:
    '''Insert historic data into the tb_historico table'''

    @classmethod
    def insert_historic(cls, df):
        try:
            DatabaseConnector.connect()
            
            table = Table('tb_historico', DatabaseConnector.metadata, autoload_with=DatabaseConnector.engine)
            
            with DatabaseConnector.connection.begin() as transaction:
                for index, row in df.iterrows():

                    insert_statement = table.insert().values(
                        date_information=row['Date'],
                        open=row['Open'],
                        high=row['High'],
                        low=row['Low'],
                        close=row['Close'],
                        volume=row['Volume'],
                        dividends=row['Dividends'],
                        stock_splits=row['Stock Splits'],
                        company_code=row['CompanyCode']
                    )

                    DatabaseConnector.connection.execute(insert_statement)
            
            print("Data inserted successfully")

        except Exception as e:
            print("Error inserting data: ", e)
