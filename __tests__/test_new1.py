import pytest
import serial
import pyautogui

# Create Serial port object called Arduino_Serial
Arduino_Serial = serial.Serial('com12', 9600)

def test_serial_communication():
    # Send 'next' command and check if it performs 'ctrl+pgdn' operation
    Arduino_Serial.write(b'next\n')
    assert pyautogui.hotkey('ctrl', 'pgdn') == 'next'

    # Send 'previous' command and check if it performs 'ctrl+pgup' operation
    Arduino_Serial.write(b'previous\n')
    assert pyautogui.hotkey('ctrl', 'pgup') == 'previous'

    # Send 'down' command and check if it scrolls down the page
    Arduino_Serial.write(b'down\n')
    assert pyautogui.scroll(-100) == 'down'

    # Send 'up' command and check if it scrolls up the page
    Arduino_Serial.write(b'up\n')
    assert pyautogui.scroll(100) == 'up'

    # Send 'change' command and check if it performs 'alt+tab' operation
    Arduino_Serial.write(b'change\n')
    assert pyautogui.keyDown('alt') == 'change'
    assert pyautogui.press('tab') == 'change'
    assert pyautogui.keyUp('alt') == 'change'
