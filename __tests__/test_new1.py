import os

os.environ['DISPLAY'] = ':0'

import unittest
import subprocess
import time
from unittest.mock import patch, MagicMock
import serial
import pyautogui
from xvfbwrapper import Xvfb 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebpage(unittest.TestCase):

    def setUp(self):
        self.vdisplay = Xvfb(width=1280, height=720)
        self.vdisplay.start()
        self.display_num = os.environ['DISPLAY']
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1280, 720)

    def tearDown(self):
        self.driver.quit()
        self.vdisplay.stop()

    def test_webpage(self):
        self.driver.get('https://www.google.com/')
        self.assertIn('Google', self.driver.title)

        search_bar = self.driver.find_element_by_name('q')
        search_bar.send_keys('OpenAI')
        search_bar.send_keys(Keys.RETURN)

        time.sleep(2)
        self.assertIn('OpenAI', self.driver.title)

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
