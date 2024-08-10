from data_extractor.db.database_connector import DatabaseConnector
from sqlalchemy import text

class HistoricRepository:
    '''Insert historic data into the tb_historico table'''

    @classmethod
    def insert_historic(cls, df):
        conn = None
        try:
            conn = DatabaseConnector.connect()
            with conn.begin() as transaction:
                for index, row in df.iterrows():
                    conn.execute(
                        text('''
                            INSERT INTO tb_historico (
                                date_information,
                                open,
                                high,
                                low,
                                close,
                                volume,
                                dividends,
                                stock_splits,
                                company_code
                            ) VALUES (
                                :date_information,
                                :open,
                                :high,
                                :low,
                                :close,
                                :volume,
                                :dividends,
                                :stock_splits,
                                :company_code
                            )
                             ON CONFLICT (date_information, open, high, low, close, volume, dividends, stock_splits, company_code)
                                DO NOTHING;;
                        '''),
                        {
                            "date_information": row['Date'], 
                            "open": row['Open'], 
                            "high": row['High'],
                            "low": row['Low'],
                            "close": row['Close'],
                            "volume": row['Volume'],
                            "dividends": row['Dividends'],
                            "stock_splits": row['Stock Splits'],
                            "company_code": row['CompanyCode']
                        }
                    )
                transaction.commit()
                print("Data inserted successfully")
        except Exception as e:
            if conn:
                conn.rollback() 
            print("Error inserting data: ", e)
        finally:
            if conn:
                conn.close()
