from general_information_extractor.src.drive.http_requester import HttpRequester
from general_information_extractor.src.drive.html_finder import HtmlFinder
from general_information_extractor.src.errors.extract_error import ExtractError

class GeneralExtractor:
    '''a class for extract the essential information from the HTML'''
    def __init__(self) -> None:
        self.__http_requester = HttpRequester()
        self.__html_finder = HtmlFinder()

    def extract(self, url, company_code):
        try:
            html_text = self.__http_requester.request(url, company_code)
            essential_information = self.__html_finder.find_essential_html(html_text)

            return essential_information
        
        except Exception as exception:
            raise ExtractError(str(exception))