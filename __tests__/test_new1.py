import pytest
import serial
import pyautogui

# Create Serial port object called Arduino_Serial
Arduino_Serial = serial.Serial('com12', 9600)

def test_serial_communication():
    # Send 'next' command and check if it performs 'ctrl+pgdn' operation
    Arduino_Serial.write(b'next\n')
    assert pyautogui.hotkey('ctrl', 'pgdn') == b'next\n'

    # Send 'previous' command and check if it performs 'ctrl+pgup' operation
    Arduino_Serial.write(b'previous\n')
    assert pyautogui.hotkey('ctrl', 'pgup') == b'previous\n'

    # Send 'down' command and check if it scrolls down the page
    Arduino_Serial.write(b'down\n')
    assert pyautogui.scroll(-100) == b'down\n'

    # Send 'up' command and check if it scrolls up the page
    Arduino_Serial.write(b'up\n')
    assert pyautogui.scroll(100) == b'up\n'

    # Send 'change' command and check if it performs 'alt+tab' operation
    Arduino_Serial.write(b'change\n')
    assert pyautogui.keyDown('alt') == b'change\n'
    assert pyautogui.press('tab') == b'change\n'
    assert pyautogui.keyUp('alt') == b'change\n'
