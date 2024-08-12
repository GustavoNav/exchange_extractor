from data_extractor.real_time_extractor.src.drive.api_requester import ApiRequester
from data_extractor.real_time_extractor.src.errors.extract_error import ExtractError

class ExtractRealTime:
    def __init__(self) -> None:
        self.__api_requester = ApiRequester()

    def extract(self, company_code: str):
        try:
            data = self.__api_requester.request(company_code)        
            return data
        
        except Exception as exception:
            raise ExtractError(str(exception))