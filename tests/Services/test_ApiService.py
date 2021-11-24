from unittest.mock import patch, MagicMock
from src.Services.ApiService import ApiService


@patch('src.infrastructure.ListEndpointReader.RequestsChunkedListEndpointReader')
@patch('src.infrastructure.ObjectWriter.CsvFileWriter')
def test_calls_read_api(api_reader_mock, csv_writer_mock):
    api_reader_instance = MagicMock()
    api_reader_instance.read_endpoint = MagicMock(return_value=[])
    api_reader_mock.return_value = api_reader_instance
    csv_writer_instance = MagicMock()
    csv_writer_instance.write_object = MagicMock()
    csv_writer_mock.return_value = csv_writer_instance
    ApiService(api_reader_instance, csv_writer_instance).run()
    assert api_reader_instance.read_endpoint.call_count == 1
    assert csv_writer_instance.write_object.call_count == 0
