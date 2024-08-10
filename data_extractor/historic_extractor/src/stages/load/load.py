from data_extractor.historic_extractor.src.db.historic_repository import HistoricRepository
from data_extractor.historic_extractor.src.errors.load_error import LoadError

class LoadData:

    def load(self, df):
        try:
            HistoricRepository.insert_historic(df)
        except Exception as exception:
            raise LoadError(str(exception))