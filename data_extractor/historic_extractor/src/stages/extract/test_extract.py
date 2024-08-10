from .extract import HistoricExtractor
import pandas as pd

def test_extract_01():
    '''Test normal case'''
    historic_extractor = HistoricExtractor()

    df = historic_extractor.extract("PETR4.SA")

    assert isinstance(df, pd.DataFrame)
    print(df.columns)
    print(df)

def test_extract_02():
    '''Test empty index'''
    historic_extractor = HistoricExtractor()

    df = historic_extractor.extract("412")
