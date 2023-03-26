import pytest
from unittest.mock import patch, Mock
import serial
import pyautogui
import io
import sys

def test_gesture_control(mocker):
    mock_serial_instance = Mock(spec=serial.Serial)
    mocker.patch('serial.Serial', return_value=mock_serial_instance)

    mock_hotkey = mocker.patch('pyautogui.hotkey')
    mock_scroll = mocker.patch('pyautogui.scroll')
    mock_keydown = mocker.patch('pyautogui.keyDown')
    mock_keyup = mocker.patch('pyautogui.keyUp')

    test_cases = [
        ("next", pyautogui.hotkey('ctrl', 'pgdn')),
        ("previous", pyautogui.hotkey('ctrl', 'pgup')),
        ("down", pyautogui.scroll(-10)),
        ("up", pyautogui.keyDown('pg up'), pyautogui.keyUp('pg up')),
        ("change", pyautogui.keyDown('alt'), pyautogui.press('tab'), pyautogui.keyUp('alt'))
    ]
    serial_data = ["{}".format(test_case[0]).encode('utf-8') for test_case in test_cases]
    mock_serial_instance.readline.side_effect = serial_data

    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        exec(open('gesture_control.py').read())
        output = fake_out.getvalue()

    for i in range(len(test_cases)):
        assert test_cases[i][0] in output
        if len(test_cases[i]) > 1:
            mock_hotkey.assert_any_call(*test_cases[i][1])
            mock_scroll.assert_any_call(*test_cases[i][1])
            mock_keydown.assert_any_call(*test_cases[i][1])
            mock_keyup.assert_any_call(*test_cases[i][1])

                self.assertIn(test_cases[i][1], mock_hotkey.mock_calls)

if __name__ == '__main__':
    unittest.main()
