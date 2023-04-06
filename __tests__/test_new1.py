import unittest
from unittest.mock import MagicMock
import io
import sys



class TestMyCode(unittest.TestCase):

    def setUp(self):
        # create a mock serial object
        self.mock_serial = MagicMock()
        # set the return value of readline() method
        self.mock_serial.readline.side_effect = [
            b'next\r\n', b'up\r\n', b'previous\r\n', b'down\r\n', b'close\r\n'
        ]
        # set the mock serial object to be used by the code
        new1.Arduino_Serial = self.mock_serial

        # redirect stdout to a StringIO object
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_new1(self):
        # test 'next' command
        new1.incoming_data = ""
        new1.Arduino_Serial.readline.return_value = b'next\r\n'
        new1.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='ctrl', up='ctrl')\nKeyboardEvent(down='pgdn', up='pgdn')"
        )

        # test 'up' command
        new1.incoming_data = ""
        new1.Arduino_Serial.readline.return_value = b'up\r\n'
        new1.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='pgup', up='pgup')"
        )

        # test 'previous' command
        new1.incoming_data = ""
        new1.Arduino_Serial.readline.return_value = b'previous\r\n'
        new1.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='ctrl', up='ctrl')\nKeyboardEvent(down='pgup', up='pgup')"
        )

        # test 'down' command
        new1.incoming_data = ""
        new1.Arduino_Serial.readline.return_value = b'down\r\n'
        new1.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='pgdn', up='pgdn')"
        )

        # test 'close' command
        new1.incoming_data = ""
        new1.Arduino_Serial.readline.return_value = b'close\r\n'
        new1.main()
        self.assertEqual(
            self.captured_output.getvalue().strip(),
            "KeyboardEvent(down='alt', up='alt')\nKeyboardEvent(down='f4', up='f4')"
        )
