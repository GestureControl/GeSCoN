import unittest
from unittest.mock import MagicMock
import io
import sys

import my_code

class TestMyCode(unittest.TestCase):

    def setUp(self):
        # create a mock serial object
        self.mock_serial = MagicMock()
        # set the return value of readline() method
        self.mock_serial.readline.side_effect = [
            b'next\r\n', b'up\r\n', b'previous\r\n', b'down\r\n', b'close\r\n'
        ]
        # set the mock serial object to be used by the code
        my_code.Arduino_Serial = self.mock_serial

        # redirect stdout to a StringIO object
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_new1(self):
        # test 'next' command
        my_code.incoming_data = ""
        my_code.Arduino_Serial.readline.return_value = b'next\r\n'
        my_code.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='ctrl', up='ctrl')\nKeyboardEvent(down='pgdn', up='pgdn')"
        )

        # test 'up' command
        my_code.incoming_data = ""
        my_code.Arduino_Serial.readline.return_value = b'up\r\n'
        my_code.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='pgup', up='pgup')"
        )

        # test 'previous' command
        my_code.incoming_data = ""
        my_code.Arduino_Serial.readline.return_value = b'previous\r\n'
        my_code.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='ctrl', up='ctrl')\nKeyboardEvent(down='pgup', up='pgup')"
        )

        # test 'down' command
        my_code.incoming_data = ""
        my_code.Arduino_Serial.readline.return_value = b'down\r\n'
        my_code.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='pgdn', up='pgdn')"
        )

        # test 'close' command
        my_code.incoming_data = ""
        my_code.Arduino_Serial.readline.return_value = b'close\r\n'
        my_code.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='alt', up='alt')\nKeyboardEvent(down='f4', up='f4')"
        )
