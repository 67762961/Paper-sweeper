import Lib
import Task_SisFoster
import time
import ctypes
import win32api
import win32con
import win32gui
import sys
import pyautogui
import win32process
import config
from Task_LogIn import LogIn
from Task_SignIn import MainTask_Signin

# 全局变量 窗口句柄列表
hwnds = []


def Init():
    """
    初始化 获取窗口句柄
    """
    global hwnds
    user32 = ctypes.windll.user32

    # 首先获取游戏窗口句柄列表
    try:
        hwnds = Lib.Find_windows("阴阳师-网易游戏")
        if len(hwnds) == 2:
            print("INIT- ***** 已经获取到两个游戏窗口")
    except:
        print("EROR- XXXXX 未找到 两个窗口 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    return hwnds


def Main_Login_2():
    """
    双账号登录
    """
    while not config.stop_thread:
        try:
            ctypes.windll.user32.SetForegroundWindow(hwnds[0])
            time.sleep(1)
            LogIn("master", hwnds[0])
            print("INFO- ***** 主账号 登录成功 ********************************")
        except:
            print("EROR- XXXXX 主账号 登录失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            config.stop_thread = True

        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "left")
        print("INIT- ····· 主账号窗口位置和大小已修改")
        break

    while not config.stop_thread:
        try:
            ctypes.windll.user32.SetForegroundWindow(hwnds[1])
            time.sleep(1)
            LogIn("slaves", hwnds[1])
            print("INFO- ***** 从账号 登录成功 ********************************")
        except:
            print("EROR- XXXXX 从账号 登录失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            config.stop_thread = True

        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "right")
        print("INIT- ····· 从账号窗口位置和大小已修改")

        break


def Sign_In():
    """
    邮箱奖励与庭院收菜
    """
    while not config.stop_thread:
        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[0])
        MainTask_Signin(hwnds[0])

        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[1])
        MainTask_Signin(hwnds[1])

        break


def Sis_Foster():
    """
    结界收菜种菜
    """
    while not config.stop_thread:
        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[0])
        Task_SisFoster.MainTask_Sisfoster(hwnds[0])

        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[1])
        Task_SisFoster.MainTask_Sisfoster(hwnds[1])

        break


def Full_operation():
    Main_Login_2()
    Sign_In()
    Sis_Foster()
