import serial
import pyautogui
from pyvirtualdisplay import Display
import pytest
import os
# Set DISPLAY environment variable
os.environ['DISPLAY'] = ':0'
# Define the test function
def test_serial_operations():
    
    
    # Start virtual display
    display = Display(visible=0, size=(1024, 768))
    display.start()

    # Open a virtual serial port
    Arduino_Serial = serial.Serial('com12',9600)
    
    # Loop for reading incoming data from the serial port
    while True:
        incoming_data = str(Arduino_Serial.readline())
        print(incoming_data)
        
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

    # Close the serial port and stop XVFB display after the test completes
    Arduino_Serial.close()
    display.stop()
    
# Define the teardown function for pytest
def teardown_function():
    pass
