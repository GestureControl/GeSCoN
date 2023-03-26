import unittest
from unittest.mock import patch
import io
import sys

class TestArduinoSerial(unittest.TestCase):

    @patch('builtins.input', side_effect=['next', 'previous', 'down', 'up', 'change'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_serial_communication(self, mock_stdout, mock_input):
        with patch('serial.Serial'):
            import serial_communication

        expected_output = 'next\nprevious\ndown\nup\nchange\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
