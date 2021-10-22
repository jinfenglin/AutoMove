import pyautogui
import time

if __name__ == "__main__":
    max_x, max_y = pyautogui.size()
    last_x, last_y = None, None
    while True:
        x, y = pyautogui.position()
        if last_x == x and last_y == y or x == None or y == None:
            pyautogui.moveTo(max_x / 2, max_y / 2)
            pyautogui.moveTo(x, y)
        last_x, last_y = x, y
        time.sleep(10)
