from data_extractor.general_information_extractor.src.stages.extract.extract import GeneralExtractor
from data_extractor.general_information_extractor.src.stages.transform.transform import TransformInformation
from data_extractor.general_information_extractor.src.stages.load.load import LoadData


class MainPipeline:
    def __init__(self) -> None:
        '''class to run the general information extractor'''
        self.__general_extractor = GeneralExtractor()
        self.__transform_information = TransformInformation()
        self.__load_data = LoadData()

    def run_pipeline(self, url, company_code):
        essential_data = self.__general_extractor.extract(url, company_code)
        transformed_data = self.__transform_information.transform(essential_data)
        self.__load_data.load(transformed_data)