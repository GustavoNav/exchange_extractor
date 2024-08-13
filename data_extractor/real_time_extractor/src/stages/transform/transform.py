from data_extractor.real_time_extractor.src.errors.transform_error import TransformError
import pandas as pd

class TransformData:
    '''
        Transform the pd.DataFrame, adding the company code in all rows and reseting index. 
        Then return the pd.DataFrame transformed
    '''
    def transform(self, dataframe: pd.DataFrame, company_code: str):
        try:
            dataframe['company_code'] = company_code
            dataframe = dataframe.reset_index()

            return dataframe
        
        except Exception as exception:
            raise TransformError(str(exception))