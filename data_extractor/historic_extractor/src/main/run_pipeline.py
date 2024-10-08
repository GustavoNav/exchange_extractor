from historic_extractor.src.stages.extract.extract import HistoricExtractor
from historic_extractor.src.stages.transform.transform import TransformData
from historic_extractor.src.stages.load.load import LoadData

class MainPipeline:
    def __init__(self) -> None:
        '''class to run the historc extractor'''
        self.__historic_extractor = HistoricExtractor()
        self.__transform_data = TransformData()
        self.__load_data = LoadData()

    def run_pipeline(self, CompanyCode: str):
        dataframe = self.__historic_extractor.extract(CompanyCode)
        dataframe = self.__transform_data.transform(dataframe, CompanyCode)
        self.__load_data.load(dataframe)