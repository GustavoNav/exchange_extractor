from .http_requester import HttpRequester

'''Test for http request from test url'''
def test_request_01():
    http_requester = HttpRequester()

    response = http_requester.request('https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/', 'PETR4.SA')
    print(response)