from general_information_extractor.src.db.general_repository import GeneralRepository
from general_information_extractor.src.errors.load_error import LoadError

class LoadData:
    '''Load the information at database'''
    def load(self, transformed_data):
        try:
            GeneralRepository.insert_general(transformed_data)
            
        except Exception as exception:
            raise LoadError(str(exception))