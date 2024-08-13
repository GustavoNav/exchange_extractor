from db.database_connector import DatabaseConnector
from sqlalchemy import text

class GeneralRepository:

    @classmethod
    def insert_general(cls, transformed_data):
        conn = None
        try:
            conn = DatabaseConnector.connect()
            with conn.begin() as transaction:
                conn.execute(text(''' 
                    INSERT INTO tb_general_financials (
                        company_code,
                        sector,
                        net_sales,
                        net_income,
                        net_margin,
                        ebitda,
                        ebitda_margin,
                        total_assets,
                        gross_debt,
                        equity,
                        pe_ratio
                    ) VALUES(
                        :company_code,
                        :sector,
                        :net_sales,
                        :net_income,
                        :net_margin,
                        :ebitda,
                        :ebitda_margin,
                        :total_assets,
                        :gross_debt,
                        :equity,
                        :pe_ratio
                    ) ON CONFLICT (company_code)
                                    DO NOTHING;

                '''
                ),
                {
                        'company_code': transformed_data['company_code'],
                        'sector': transformed_data['sector'],
                        'net_sales': transformed_data['net_sales'],
                        'net_income': transformed_data['net_income'],
                        'net_margin': transformed_data['net_margin'],
                        'ebitda': transformed_data['ebitda'],
                        'ebitda_margin': transformed_data['ebitda_margin'],
                        'total_assets': transformed_data['total_assets'],
                        'gross_debt': transformed_data['gross_debt'],
                        'equity': transformed_data['equity'],
                        'pe_ratio': transformed_data['pe_ratio']
                }
            )
            conn.commit()
            print("Data inserted successfully into tb_general_financials")
        except Exception as e:
            if conn:
                conn.rollback() 
            print("Error inserting data: ", e)
        finally:
            if conn:
                conn.close()