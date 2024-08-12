from .api_requester import ApiRequester

def test_request_01():
    api_requester = ApiRequester()

    data = api_requester.request('PETR3.SA')

    print(data)