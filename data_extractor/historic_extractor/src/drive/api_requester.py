import yfinance as yf

class ApiRequester:
    '''Get data from API and return pd.DataFrame'''

    def request(self, company_code: str):

        acao = yf.Ticker(company_code)
        historico_precos = acao.history(period="max")

        return historico_precos