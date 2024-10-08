from historic_extractor.src.db.historic_repository import HistoricRepository
from historic_extractor.src.errors.load_error import LoadError

class LoadData:
    '''Insert dataframe into Database'''
    def load(self, df):
        try:
            HistoricRepository.insert_historic(df)
        except Exception as exception:
            raise LoadError(str(exception))