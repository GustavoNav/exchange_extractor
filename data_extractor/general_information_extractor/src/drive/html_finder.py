from bs4 import BeautifulSoup

class HtmlFinder:
    '''A class for collecting the essential information from the html '''

    def find_essential_html(self, data):
        soup = BeautifulSoup(data['html'], 'html.parser')
        
        essential_information = str(soup.find_all('div',class_="about mt-5"))

        essential_data = {'company_code': data['company_code'], 'essential_information': essential_information}

        return essential_data