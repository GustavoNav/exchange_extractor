import pandas as pd
from .api_requester import ApiRequester

def test_request_01():
    '''result of extraction'''
    api_requester = ApiRequester()

    company_code = "PETR4.SA"

    historico = api_requester.request(company_code)

    print(historico)

