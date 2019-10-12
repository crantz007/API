import unittest
from unittest import TestCase
from unittest.mock import patch
import Bitcoin


class TestBitCoin(TestCase):
    @patch('Bitcoin.get_bitcoin_rate')
    def test_get_price_in_us_dollar(self, mock_rates):

        mock_rate = 12345.67
        example_api_response = {'rate': mock_rate}
        mock_rates.side_effect = [example_api_response]
        bitcoins = float(Bitcoin.get_bitcoin())
        formatting = bitcoins * mock_rate
        conversion = Bitcoin.convert(mock_rate,bitcoins)
        self.assertEqual(formatting, conversion)


if __name__ == '__main__':
    unittest.main()
