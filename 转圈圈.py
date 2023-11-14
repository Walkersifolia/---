import ctypes
import win32api, win32con
import time

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

if is_admin():
    print("使用说明:\n\n按住鼠标第二侧键开转（这通常是靠近鼠标前端的侧键）\n\n作者：圈圈  B站：Walker_Tian")

    while True:
        if win32api.GetKeyState(win32con.VK_XBUTTON2) < 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,800,0,0,0)
        time.sleep(0.01)
else:
    print("请以管理员模式运行此程序")
    input("按Enter回车键退出程序...")