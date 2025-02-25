import unittest

from unittest.mock import patch, MagicMock
from src.sqs_queues import get_queues_message_totals

class TestSQSQueueTotals(unittest.TestCase):


    @patch('sqs_queues.boto3.client')
    def test_get_queue_message_count_error(self, mock_client):
        mock_sqs = MagicMock()
        mock_client.return_value = mock_sqs
        mock_sqs.get_queue_attributes.side_effect = Exception("Some error")
        count = get_queue_message_count(mock_sqs, "some_url")
        self.assertEqual(count, 0)


    @patch('sqs_queues.boto3.client')
    def test_get_queue_message_count_happy_case(self, mock_client):




if __name__ == '__main__':
    import json #Import json here for the test file
    from src.sqs_queues import get_queue_message_count
    unittest.main()