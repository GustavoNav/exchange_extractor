from data_extractor.real_time_extractor.src.stages.extract.extract import ExtractRealTime
from data_extractor.real_time_extractor.src.stages.transform.transform import TransformData
from data_extractor.real_time_extractor.src.stages.load.load import LoadData

class MainPipeline:
    def __init__(self) -> None:
        self.__extract_real_time = ExtractRealTime()
        self.__transform_data = TransformData()
        self.__load_data = LoadData()

    def run_pipeline(self, company_code: str):
        data = self.__extract_real_time.extract(company_code)
        transformed_data = self.__transform_data.transform(data, company_code)
        self.__load_data.load(transformed_data)
