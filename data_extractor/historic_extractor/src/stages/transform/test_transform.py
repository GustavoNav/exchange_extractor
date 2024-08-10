import pandas as pd
from .transform import TransformData


'''Test transformation'''
def test_01():
    transform_data = TransformData()

    data = [
        ['2000-01-03 00:00:00-02:00', 1.402440, 1.402440, 1.402440, 1.402440, 35389440000, 0.0, 0.0],
        ['2000-01-04 00:00:00-02:00', 1.324858, 1.324858, 1.324858, 1.324858, 28861440000, 0.0, 0.0],
        ['2000-01-05 00:00:00-02:00', 1.311490, 1.311490, 1.311490, 1.311490, 43033600000, 0.0, 0.0]
    ]
    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']

    df = pd.DataFrame(data, columns=columns)
    
    transform_data.transform(df, 'PTR4.SA')


'''Test wrong type'''
def test_02():
    transform_data = TransformData()

    df = 'wrong type'
    
    transform_data.transform(df, 'PTR4.SA')