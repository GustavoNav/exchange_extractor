from .database_repository import DatabaseRepository

def test_select_historic():
    DatabaseRepository.select_historic(['VALE3.SA', 'CSNA3.SA', 'USIM5.SA', 'PETR3.SA'])

def test_select_general_financials():
    DatabaseRepository.select_general_financials(['VALE3.SA', 'CSNA3.SA', 'USIM5.SA', 'PETR3.SA'])

def test_select_real_time():
    DatabaseRepository.select_real_time(['VALE3.SA', 'CSNA3.SA', 'USIM5.SA', 'PETR3.SA'])
