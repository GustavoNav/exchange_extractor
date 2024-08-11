from .general_repository import GeneralRepository

def test_insert_general_01():
    transformed_data = {'company_code': 'PTR4.SA', 'sector': 'Petróleo E Gás', 'net_sales': 499060000000.0, 'net_income': 79210000000.0, 'net_margin': 15.87, 'ebitda': 240730000000.0, 'ebitda_margin': '48.23', 'total_assets': 1058680000000.0001, 'gross_debt': 331470000000.0, 'equity': 376040000000.0, 'pe_ratio': 6.0}
    GeneralRepository.insert_general(transformed_data)