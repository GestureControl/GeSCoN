import unittest
from unittest.mock import MagicMock, patch

import serial
import pyautogui

class TestSerialCommunication(unittest.TestCase):

    @patch('serial.Serial')
    @patch('pyautogui.hotkey')
    @patch('pyautogui.scroll')
    @patch('pyautogui.keyDown')
    @patch('pyautogui.keyUp')
    def test_new1(self, mock_keyUp, mock_keyDown, mock_scroll, mock_hotkey, mock_serial):
        
        # Set up mock serial object and input
        mock_serial.return_value.readline.return_value = b'next\n'
        
        # Call the function to be tested
        main()
        
        # Check that expected functions were called with expected inputs
        mock_serial.assert_called_with('com5', 9600)
        mock_serial.return_value.readline.assert_called()
        mock_hotkey.assert_called_with('ctrl', 'pgdn')
        mock_keyUp.assert_not_called()
        mock_keyDown.assert_not_called()
        mock_scroll.assert_not_called()
