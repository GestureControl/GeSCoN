import os
os.environ['DISPLAY'] = ':0'
from xvfbwrapper import Xvfb
import pytest
from unittest.mock import patch, Mock
import serial
import pyautogui
import io
import sys

@pytest.fixture(scope="module")
def xvfb():
    vdisplay = Xvfb()
    vdisplay.start()
    yield vdisplay
    vdisplay.stop()

def test_screenshot(xvfb):
    # Move the mouse to the center of the screen
    screen_width, screen_height = pyautogui.size()
    center_x = int(screen_width / 2)
    center_y = int(screen_height / 2)
    pyautogui.moveTo(center_x, center_y)

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Assert that the screenshot was taken
    assert screenshot is not None

def test_mouse_movement(xvfb):
    # Move the mouse to the center of the screen
    screen_width, screen_height = pyautogui.size()
    center_x = int(screen_width / 2)
    center_y = int(screen_height / 2)
    pyautogui.moveTo(center_x, center_y)

    # Move the mouse to a new location
    new_x, new_y = center_x + 50, center_y + 50
    pyautogui.moveTo(new_x, new_y)

    # Assert that the mouse was moved
    assert pyautogui.position() == (new_x, new_y)
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
