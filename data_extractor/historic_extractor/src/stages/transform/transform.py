import pandas as pd
from historic_extractor.src.errors.transform_error import TransformError

class TransformData:
    '''Transform extracted data'''
    def transform(self, dataframe: pd.DataFrame, CompanyCode: str):
        try:
            dataframe["CompanyCode"] = CompanyCode
            dataframe = dataframe.reset_index()
            return dataframe
        
        except Exception as exception:
            raise TransformError(str(exception))