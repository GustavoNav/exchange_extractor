from .load import LoadData
import pandas as pd

'''Test normal df case'''
def test_load_01():
    load_data = LoadData()

    data = [
        ['2000-01-04 00:00:00-02:00', 1.324858, 1.324858, 1.324858, 1.324858, 28861440000, 0.0, 0.0, 'PETR3.SA'],
        ['2000-01-05 00:00:00-02:00', 1.311490, 1.311490, 1.311490, 1.311490, 43033600000, 0.0, 0.0, 'PETR3.SA']
    ]
    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits', 'CompanyCode']

    df = pd.DataFrame(data, columns=columns)

    load_data.load(df)