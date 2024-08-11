from data_extractor.general_information_extractor.src.main import main_pipeline

def run_general_pipeline(url, company_code):
    main_pipeline.run_pipeline(url, company_code)

run_general_pipeline('https://www.infomoney.com.br/cotacoes/b3/acao/3rpetroleum-rrrp3/', 'RRRP3.SA')