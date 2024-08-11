from .http_requester import HttpRequester
from .html_finder import HtmlFinder

'''Test for collect essential information'''
def test_finder_essenial_html():
    http_requester = HttpRequester()
    response = http_requester.request('https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/', 'PTR4.SA')

    html_finder = HtmlFinder()
    essential_data = html_finder.find_essential_html(response)
    print(essential_data)