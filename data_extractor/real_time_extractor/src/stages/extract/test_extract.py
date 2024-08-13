from .extract import ExtractRealTime

'''test extraction, then print the pd.DataFrame'''
def test_extract_01():
    extract_real_time = ExtractRealTime()
    data = extract_real_time.extract('PETR3.SA')
    print(data)