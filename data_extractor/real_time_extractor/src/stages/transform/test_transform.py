from .transform import TransformData
from .mock_data import mock_data

'''test the transformation, using the mock_data.'''
def test_transform_01():
    transform_data = TransformData()
    transformed_data = transform_data.transform(mock_data, 'PETR3.SA')

    print(transformed_data)