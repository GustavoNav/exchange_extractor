from .extract import GeneralExtractor

'''test extract from a url '''
def test_extract_01():
    general_extractor = GeneralExtractor()

    essential_information = general_extractor.extract('https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/', 'PETR4.SA')

    print(essential_information)