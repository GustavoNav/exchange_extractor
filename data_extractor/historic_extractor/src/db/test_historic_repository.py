from .historic_repository import HistoricRepository
import pandas as pd

def test_01():
    historic_repository = HistoricRepository()

    data = [
        ['2000-01-04 00:00:00-02:00', 1.324858, 1.324858, 1.324858, 1.324858, 28861440000, 0.0, 0.0, 'PETR3.SA'],
        ['2000-01-05 00:00:00-02:00', 1.311490, 1.311490, 1.311490, 1.311490, 43033600000, 0.0, 0.0, 'PETR3.SA']
    ]
    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits', 'CompanyCode']

    df = pd.DataFrame(data, columns=columns)

    historic_repository.insert_historic(df)