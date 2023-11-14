import win32api, win32con
from pynput import mouse
import threading

x2_pressed = False
move_thread = None

def on_click(x, y, button, pressed):
    global x2_pressed, move_thread
    if button == mouse.Button.x2:
        x2_pressed = pressed
        if pressed:
            move_thread = threading.Thread(target=move_mouse)
            move_thread.start()
        else:
            if move_thread is not None:
                move_thread.join()

def move_mouse():
    while x2_pressed:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 800, 0, 0, 0)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
