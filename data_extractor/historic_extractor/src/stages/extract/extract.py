import pandas as pd
from src.drive.api_requester import ApiRequester
from src.errors.extract_error import ExtractError

class HistoricExtractor:
    '''execute data extraction'''

    def __init__(self) -> None:
        self.__api_requester = ApiRequester()

    def extract(self, company_code: str):
        try:
            data = self.__api_requester.request(company_code)

            if data.empty:
                raise ExtractError("DataFrame is empty")
            
            return data
        
        except Exception as exception:
            raise ExtractError(str(exception))

       