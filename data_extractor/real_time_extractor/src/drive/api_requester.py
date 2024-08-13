import yfinance as yf

class ApiRequester:
    '''
        Request historical data of the day from the API yfinance, with 1 minute intervals.
        Return pd.DataFrame object. 
    '''
    def request(self, company_code: str):
        period = "1d"
        interval = "1m"

        historical_data = yf.Ticker(company_code).history(period, interval, actions=False).dropna()

        return historical_data