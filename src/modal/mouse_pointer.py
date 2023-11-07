import pyautogui, threading, time
from .pointer import Pointer

class MousePointer(Pointer):

    def __init__(self):
        super().__init__()
        
        self.running = True
        self.thread = threading.Thread(target=self.update, daemon=True)

    def start(self, app_name):
        window = pyautogui.getWindowsWithTitle(app_name)[0]
        self.window = window

        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def update(self):
        while self.running:
            time.sleep(0.1)

            if not self.window.isActive:
                continue

            x, y = pyautogui.position()
            tl_x = self.window.left
            tl_y = self.window.top
            br_x = self.window.left + self.window.width
            br_y = self.window.top + self.window.height

            self.window_bounds = (tl_x, tl_y, self.window.width, self.window.height)

            if tl_x <= x <= br_x and tl_y <= y <= br_y:
                # convert to relative coordinates
                self.x = x - tl_x
                self.y = y - tl_y
                self.callback(self.x, self.y)
            
            

if __name__ == "__main__":
    pointer = MousePointer()
    pointer.on_update(lambda x, y: print(f"Pointer moved to ({x}, {y})"))

    pointer.start("Visual Studio Code")
    input()
    print("Stopping...")
    pointer.stop()