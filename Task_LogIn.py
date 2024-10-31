import time
import pyautogui
import ctypes
import win32gui
import config
from Lib import Find_in_windows, Find_in_screen, Find_Click_screen, Click


def LogIn(Log, Hwnd):
    """
    账号的登录 默认上次登录更晚的是副账号
    :return:    1正常0异常
    """
    win32gui.SetWindowPos(Hwnd, 0, 960, 540, 1920, 1158, 0x0040)
    time.sleep(1)
    # 先检测是否已经登录

    if Find_in_windows(Hwnd, "./pic/Main/Zhujiemian.png", 0.05, 0):
        print("检测到进入庭院 跳过登录")
        return 1
    else:
        print("准备登录")

    Wait = 0
    while True:
        Range = Find_in_screen("./pic/Main/Dengluzhujiemian.png", 0.05, 0)
        if Range:
            print("检测到登录界面")
            break
        else:
            Wait += 1
            print("未检测到登录界面 等待:", Wait)
            time.sleep(1)
            ctypes.windll.user32.SetForegroundWindow(Hwnd)

        if Wait >= 30:
            print("EROR- XXXXX 登录失败超时退出 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            config.stop_thread = True
            break

        # 逐步点击登录
    while not config.stop_thread:
        if Log == "master":
            # 注：此处条件可以极为苛刻 一般识别取值为0.002
            Find_Click_screen("./pic/Main/Qiehuanzhanghao.png", 0.005, "打开账号列表", "无法打开账号列表")

            # 注：此处条件可以极为苛刻 一般识别取值为0.000
            Find_Click_screen("./pic/Main/Zhuzhanghao.png", 0.005, "选择主账号", "无法识别主账号区域")
            time.sleep(1)
            Find_Click_screen("./pic/Main/Jinruyouxi0.png", 0.05, "点击账号登录", "账号未登录")
        else:
            Find_Click_screen("./pic/Main/Jinruyouxi.png", 0.05, "点击账号登录", "账号未登录")
        time.sleep(1)
        Find = Find_in_screen("./pic/Main/Jinruyouxi1.png", 0.05, 0)
        if not Find:
            print("无法识别 尝试坐标点击")
            # 坐标法
            Range = ((828, 907), (1112, 1007))
            Click(Hwnd, Range, 1)
            return 1
        else:
            print("识别进入游戏")
            Click(Hwnd, Find, 1)
            return 1
        break
