from .real_time_respository import RealTimeRepository
from real_time_extractor.src.stages.extract.extract import ExtractRealTime
from real_time_extractor.src.stages.transform.transform import TransformData

def test_insert_01():
    extract_real_time = ExtractRealTime()
    transform_data = TransformData()

    data = extract_real_time.extract('PETR3.SA')
    transformed_data = transform_data.transform(data, 'PETR3.SA')
    print(transformed_data)
    RealTimeRepository.insert_real_time(transformed_data)