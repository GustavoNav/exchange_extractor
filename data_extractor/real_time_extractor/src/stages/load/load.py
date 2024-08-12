import pandas as pd
from data_extractor.real_time_extractor.src.db.real_time_respository import RealTimeRepository
from data_extractor.real_time_extractor.src.errors.load_error import LoadError

class LoadData():
    
    def load(self, data: pd.DataFrame):
        try:
            RealTimeRepository.insert_real_time(data)
        except Exception as exception:
            raise LoadError(str(exception))