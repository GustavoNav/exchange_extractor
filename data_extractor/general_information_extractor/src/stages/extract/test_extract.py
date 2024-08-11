from .extract import GeneralExtractor

def test_extract_01():
    general_extractor = GeneralExtractor()

    essential_information = general_extractor.extract('https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/')

    print(essential_information)