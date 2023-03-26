import unittest
import subprocess
import time
from unittest.mock import patch, MagicMock
import serial
import pyautogui
from xvfbwrapper import Xvfb 
import os

os.environ['DISPLAY'] = ':0'

class TestMyCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.vdisplay = Xvfb() 
        cls.vdisplay.start()  
        time.sleep(1)
        
    @classmethod
    def tearDownClass(cls):
        cls.vdisplay.stop()  #    

class TestSerialCommands(unittest.TestCase):
    
    @patch('serial.Serial')
    @patch('builtins.print')
    @patch('pyautogui.hotkey')
    @patch('pyautogui.scroll')
    @patch('pyautogui.keyDown')
    @patch('pyautogui.keyUp')
    def test_new1(self, mock_keyUp, mock_keyDown, mock_scroll, mock_hotkey, mock_print, mock_Serial):
        # Set up the mock Serial object and define incoming data for the different test cases
        mock_serial = MagicMock(spec=serial.Serial)
        mock_Serial.return_value = mock_serial
        incoming_data_next = "next"
        incoming_data_previous = "previous"
        incoming_data_down = "down"
        incoming_data_up = "up"
        incoming_data_change = "change"
        
        # Test case for "next" command
        mock_serial.readline.return_value = incoming_data_next.encode()
        test_next = SerialCommands()
        test_next.read_serial()
        mock_hotkey.assert_called_once_with('ctrl', 'pgdn')
        
        # Test case for "previous" command
        mock_serial.readline.return_value = incoming_data_previous.encode()
        test_previous = SerialCommands()
        test_previous.read_serial()
        mock_hotkey.assert_called_once_with('ctrl', 'pgup')
        
        # Test case for "down" command
        mock_serial.readline.return_value = incoming_data_down.encode()
        test_down = SerialCommands()
        test_down.read_serial()
        mock_scroll.assert_called_once_with(-10)
        
        # Test case for "up" command
        mock_serial.readline.return_value = incoming_data_up.encode()
        test_up = SerialCommands()
        test_up.read_serial()
        mock_keyDown.assert_called_once_with('pg up')
        mock_keyUp.assert_called_once_with('pg up')
        
        # Test case for "change" command
        mock_serial.readline.return_value = incoming_data_change.encode()
        test_change = SerialCommands()
        test_change.read_serial()
        mock_keyDown.assert_called_once_with('alt')
        mock_press.assert_called_once_with('tab')
        mock_keyUp.assert_called_once_with('alt')

        
if __name__ == '__main__':
    unittest.main()        
