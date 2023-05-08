import serial
import pyautogui
import sys
class SerialControlledInput:
    gc_mode = False
    def __init__(self, port, baud_rate=9600):
        SerialControlledInput.gc_mode = True
        self.serial_port = serial.Serial(port, baud_rate)
        self.current_input = ""

    def read_input(self):
        self.current_input = self.serial_port.readline().decode().strip()

    def process_input(self):
        if 'next' in self.current_input:
            pyautogui.hotkey('ctrl', 'pgdn')
        elif 'previous' in self.current_input:
            pyautogui.hotkey('ctrl', 'pgup')
        elif 'down' in self.current_input:
            pyautogui.scroll(-100)
        elif 'up' in self.current_input:
            pyautogui.scroll(100)
        elif 'close' in self.current_input:
            pyautogui.hotkey('alt', 'f4')

    def start(self):
        try:
            while SerialControlledInput.gc_mode:
                self.read_input()
                self.process_input()
                self.current_input = ""
        except serial.SerialException as e:
            print("Serial Port Error:", e)
        finally:
            self.serial_port.close()

    def stop(self):
        sys.exit()
        

# if __name__ == '__main__':
#     input_controller = SerialControlledInput('com5')
#     input_controller.start()