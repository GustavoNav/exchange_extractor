import requests


class HttpRequester:
    ''' A simple class for making HTTP requests to a specified URL.'''

    def request(self, url, company_code):
        html = requests.get(url)
        
        data = {'company_code': company_code, 'html': html.text}
        return data