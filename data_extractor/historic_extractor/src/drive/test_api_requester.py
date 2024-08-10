from .api_requester import ApiRequester

'''Test result of extraction'''
def test_request_01():

    api_requester = ApiRequester()

    company_code = "PETR4.SA"

    historico = api_requester.request(company_code)

    print(historico)

