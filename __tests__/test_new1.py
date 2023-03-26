import unittest
from unittest.mock import Mock, patch

import serial
import pyautogui

class TestArduinoSerial(unittest.TestCase):

    @patch('serial.Serial')
    def test_next_tab(self, mock_serial):
        mock_data = b'next'
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.return_value = mock_data
        mock_serial.return_value = mock_serial_instance

        with patch('pyautogui.hotkey') as mock_hotkey:
            arduino = ArduinoSerial('com5', 9600)
            arduino.read_serial()

            mock_hotkey.assert_called_with('ctrl', 'pgdn')
    
    @patch('serial.Serial')
    def test_previous_tab(self, mock_serial):
        mock_data = b'previous'
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.return_value = mock_data
        mock_serial.return_value = mock_serial_instance

        with patch('pyautogui.hotkey') as mock_hotkey:
            arduino = ArduinoSerial('com5', 9600)
            arduino.read_serial()

            mock_hotkey.assert_called_with('ctrl', 'pgup')
    
    @patch('serial.Serial')
    def test_scroll_down(self, mock_serial):
        mock_data = b'down'
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.return_value = mock_data
        mock_serial.return_value = mock_serial_instance

        with patch('pyautogui.scroll') as mock_scroll:
            arduino = ArduinoSerial('com5', 9600)
            arduino.read_serial()

            mock_scroll.assert_called_with(-10)
    
    @patch('serial.Serial')
    def test_scroll_up(self, mock_serial):
        mock_data = b'up'
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.return_value = mock_data
        mock_serial.return_value = mock_serial_instance

        with patch('pyautogui.keyDown') as mock_keyDown, patch('pyautogui.keyUp') as mock_keyUp:
            arduino = ArduinoSerial('com5', 9600)
            arduino.read_serial()

            mock_keyDown.assert_called_with('pg up')
            mock_keyUp.assert_called_with('pg up')
    
    @patch('serial.Serial')
    def test_switch_tab(self, mock_serial):
        mock_data = b'change'
        mock_serial_instance = Mock(spec=serial.Serial)
        mock_serial_instance.readline.return_value = mock_data
        mock_serial.return_value = mock_serial_instance

        with patch('pyautogui.keyDown') as mock_keyDown, patch('pyautogui.press') as mock_press, patch('pyautogui.keyUp') as mock_keyUp:
            arduino = ArduinoSerial('com5', 9600)
            arduino.read_serial()

            mock_keyDown.assert_called_with('alt')
            mock_press.assert_called_with('tab')
            mock_keyUp.assert_called_with('alt')

if __name__ == '__main__':
    unittest.main()
