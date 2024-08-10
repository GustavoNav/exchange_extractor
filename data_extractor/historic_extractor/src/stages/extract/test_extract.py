from .extract import HistoricExtractor
import pandas as pd

'''Test normal case'''
def test_extract_01():
    historic_extractor = HistoricExtractor()

    df = historic_extractor.extract("PETR4.SA")

    assert isinstance(df, pd.DataFrame)
    print(df.columns)
    print(df)

'''Test empty index'''
def test_extract_02():
    historic_extractor = HistoricExtractor()

    df = historic_extractor.extract("412")
