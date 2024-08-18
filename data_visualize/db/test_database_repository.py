from .database_repository import DatabaseRepository

def test_select_historic():
    DatabaseRepository.select_historic(['MGLU3.SA','PETZ3.SA', 'AZUL4.SA', 'VIVT3.SA'])

def test_select_general_financials():
    DatabaseRepository.select_general_financials(['MGLU3.SA','PETZ3.SA', 'AZUL4.SA', 'VIVT3.SA'])

def test_select_real_time():
    DatabaseRepository.select_real_time(['MGLU3.SA','PETZ3.SA', 'AZUL4.SA', 'VIVT3.SA'])
