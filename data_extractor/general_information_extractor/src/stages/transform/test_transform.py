from .transform import TransformInformation
from .mock_information import mock_information

'''Test tramsformation of the mocked information'''
def test_transform_01():
    transform_information = TransformInformation()
    essential_information = mock_information

    transformed_data = transform_information.transform(essential_information)
    print(transformed_data)