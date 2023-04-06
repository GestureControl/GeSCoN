import unittest
import cv2
import mediapipe as mp
import pyautogui
export DISPLAY=:0 
class TestVirtualMouse(unittest.TestCase):

    def setUp(self):
        self.cap = cv2.VideoCapture(0)
        self.hand_detector = mp.solutions.hands.Hands()
        self.drawing_utils = mp.solutions.drawing_utils
        self.screen_width, self.screen_height = pyautogui.size()
        self.index_y = 0

    def tearDown(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def test_virtual_mouse(self):
        while True:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = self.hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks
            if hands:
                for hand in hands:
                    self.drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x*frame_width)
                        y = int(landmark.y*frame_height)
                        if id == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = self.screen_width/frame_width*x
                            self.index_y = self.screen_height/frame_height*y

                        if id == 4:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = self.screen_width/frame_width*x
                            thumb_y = self.screen_height/frame_height*y
                            print('outside', abs(self.index_y - thumb_y))
                            if abs(self.index_y - thumb_y) < 20:
                                pyautogui.click()
                                pyautogui.sleep(1)
                            elif abs(self.index_y - thumb_y) < 100:
                                pyautogui.moveTo(index_x, self.index_y)
            cv2.imshow('Virtual Mouse', frame)
            cv2.waitKey(1)

if __name__ == '__main__':
    unittest.main()
