import Lib
import Task_SignIn
import Task_SisFoster
import time
import ctypes
import win32api
import win32con
import win32gui
import sys
import pyautogui
import win32process

# 全局变量 窗口句柄列表
hwnds = []


def Init():
    """
    获取窗口句柄 并分别登录账号
    """
    global hwnds
    user32 = ctypes.windll.user32

    # --------------------------------------------------------------------------------------------------------------------------------
    # region 获取游戏窗口句柄 分别登录账号

    # 首先获取游戏窗口句柄列表
    hwnds = Lib.Find_windows("阴阳师-网易游戏")
    if len(hwnds) == 2:
        print("INIT- ····· 已经获取到两个游戏窗口")
    else:
        print("EROR- ***** 未找到 两个窗口 ********************************")
        sys.exit()
    return hwnds
    # --------------------------------------------------------------------------------------------------------------------------------
    # endregion


def WindowMov(Log, Hwnd):
    """
    修改窗口位置
    @return: 1正常0异常
    """
    Pos = win32gui.GetWindowRect(Hwnd)
    win32gui.SetWindowPos(
        Hwnd,
        0,
        960,
        540,
        1920,
        1158,
        0x0040,
    )
    if Log == "master":
        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "left")
        print("INIT- ····· 窗口位置和大小已修改")
        return 1
    else:
        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "right")
        print("INIT- ····· 窗口位置和大小已修改")
        return 1


def Login():
    # 将第一个窗口设定为前台窗口 并登录主账号
    log = Task_SignIn.LogIn("master", hwnds[0])
    if not log:
        print("EROR- ***** 主账号 登录失败 ********************************")
        sys.exit()

    # 将第二个窗口设定为前台窗口 并登录从账号
    log = Task_SignIn.LogIn("slave", hwnds[1])
    if not log:
        print("EROR- ***** 从账号 登录失败 ********************************")
        sys.exit()


def Sign_In():
    """
    邮箱奖励与庭院收菜
    """
    print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ctypes.windll.user32.SetForegroundWindow(hwnds[0])
    Task_SignIn.MainTask_Signin(hwnds[0])

    print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ctypes.windll.user32.SetForegroundWindow(hwnds[1])
    Task_SignIn.MainTask_Signin(hwnds[1])


def Sis_Foster():
    """
    结界收菜种菜
    """
    print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ctypes.windll.user32.SetForegroundWindow(hwnds[0])
    Task_SisFoster.MainTask_Sisfoster(hwnds[0])

    print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ctypes.windll.user32.SetForegroundWindow(hwnds[1])
    Task_SisFoster.MainTask_Sisfoster(hwnds[1])


def Full_operation():
    Login()
    Sign_In()
    Sis_Foster()
