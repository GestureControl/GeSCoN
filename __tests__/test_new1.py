import pytest
import os

@pytest.mark.xfail(reason="Flaky test due to GUI interaction")
def test_serial():
    os.environ['DISPLAY'] = ':0'
    with XVFB():
        import serial
        import pyautogui
        Arduino_Serial = serial.Serial('com12', 9600)
        while 1:
            incoming_data = str(Arduino_Serial.readline())
            print incoming_data
            if 'next' in incoming_data:
                pyautogui.hotkey('ctrl', 'pgdn')
            if 'previous' in incoming_data:
                pyautogui.hotkey('ctrl', 'pgup')
            if 'down' in incoming_data:
                pyautogui.scroll(-100)
            if 'up' in incoming_data:
                pyautogui.scroll(100)
            if 'change' in incoming_data:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
            incoming_data = ""

