from db.database_connector import DatabaseConnector
from sqlalchemy import text

class RealTimeRepository:
    '''Insert real time data into the tb_historico table'''

    @classmethod
    def insert_real_time(cls, df):
        conn = None
        try:
            conn = DatabaseConnector.connect()
            with conn.begin() as transaction:
                for index, row in df.iterrows():
                    conn.execute(
                        text('''
                            INSERT INTO tb_real_time (
                                company_code,
                                date_information,
                                open,
                                high,
                                low,
                                close
                            ) VALUES (
                                :company_code,
                                :date_information,
                                :open,
                                :high,
                                :low,
                                :close
                            )
                            ON CONFLICT (date_information, company_code)
                            DO NOTHING;
                        '''),
                        {
                            "company_code": row['company_code'],
                            "date_information": row['Datetime'], 
                            "open": row['Open'], 
                            "high": row['High'],
                            "low": row['Low'],
                            "close": row['Close']
                        }
                    )
                transaction.commit()
                print("Data inserted successfully into tb_real_time")
        except Exception as e:
            if conn:
                conn.rollback() 
            print("Error inserting data: ", e)
        finally:
            if conn:
                conn.close()