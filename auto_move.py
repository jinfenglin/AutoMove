import pyautogui
import time
import datetime

# pip install pyautogui
max_hours = 3
if __name__ == "__main__":
    refresh_time = time.time()
    max_x, max_y = pyautogui.size()
    last_x, last_y = None, None
    while True:
        x, y = pyautogui.position()
        passed_hours, _ = divmod(time.time() - refresh_time, 3600)
        if passed_hours >= max_hours:
            key = input("exceed maximal hours, press any key to continue ... ")
            refresh_time = time.time()

        if last_x == x and last_y == y or x == None or y == None:
            pyautogui.moveTo(max_x / 2, max_y / 2)
            pyautogui.moveTo(x, y)
        last_x, last_y = x, y
        time.sleep(150)
        print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
