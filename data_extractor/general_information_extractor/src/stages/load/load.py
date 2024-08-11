from data_extractor.general_information_extractor.src.db.general_repository import GeneralRepository
from data_extractor.general_information_extractor.src.errors.load_error import LoadError

class LoadData:
    def load(self, transformed_data):
        try:
            GeneralRepository.insert_general(transformed_data)
            
        except Exception as exception:
            raise LoadError(str(exception))