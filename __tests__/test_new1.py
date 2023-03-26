import pytest
from unittest.mock import patch, Mock
import serial
import pyautogui
import io
import sys

class TestGestureControl:
    
    @patch('serial.Serial')
    @patch('pyautogui.hotkey')
    @patch('pyautogui.scroll')
    @patch('pyautogui.keyDown')
    @patch('pyautogui.keyUp')
    def test_new1(self, mock_serial, mock_hotkey, mock_scroll, mock_keydown, mock_keyup):
        test_cases = [
            ("next", pyautogui.hotkey('ctrl', 'pgdn')),
            ("previous", pyautogui.hotkey('ctrl', 'pgup')),
            ("down", pyautogui.scroll(-10)),
            ("up", pyautogui.keyDown('pg up'), pyautogui.keyUp('pg up')),
            ("change", pyautogui.keyDown('alt'), pyautogui.press('tab'), pyautogui.keyUp('alt'))
        ]
        serial_data = ["{}".format(test_case[0]).encode('utf-8') for test_case in test_cases]
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.side_effect = serial_data
        mock_serial.return_value = mock_serial_instance

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            exec(open('gesture_control.py').read())
            output = fake_out.getvalue()

        for i in range(len(test_cases)):
            self.assertIn(test_cases[i][0], output)
            if len(test_cases[i]) > 1:
                self.assertIn(test_cases[i][1], mock_hotkey.mock_calls)
