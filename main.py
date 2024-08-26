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
import subprocess
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

    print("INIT- +++++ 程序初始化进行中 ++++++++++++++++++++++++++++++++")

    # 首先获取游戏窗口句柄列表
    try:
        hwnds = Lib.Find_windows("阴阳师-网易游戏")
        if len(hwnds) == 2:
            print("INIT- ----- 已捕获到两个窗口 --------------------------------")
        else:
            wait = 0
            while True:
                try:
                    process1 = subprocess.Popen([config.exe_path], start_new_session=True)
                    process2 = subprocess.Popen([config.exe_path], start_new_session=True)
                    # 等待进程启动
                    process1.wait()
                    process2.wait()
                    hwnds = Lib.Find_windows("阴阳师-网易游戏")
                    if len(hwnds) == 2:
                        print("INIT- ----- 启动并捕获阴阳师 --------------------------------")
                        break
                    else:
                        process1.kill()
                        process2.kill()
                        process1 = subprocess.Popen([config.exe_path], start_new_session=True)
                        process2 = subprocess.Popen([config.exe_path], start_new_session=True)
                        process1.wait()
                        process2.wait()
                        hwnds = Lib.Find_windows("阴阳师-网易游戏")
                        wait += 1
                        if len(hwnds) == 2:
                            print("INIT- ----- 启动并捕获阴阳师 --------------------------------")
                            break
                    if wait >= 3:
                        print("EROR- XXXXX 启动双开程序失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                        break
                except Exception as e:
                    print(f"启动进程或获取窗口句柄时发生异常: {e}")
    except:
        print(f"获取窗口句柄时发生异常: {e}")

    return hwnds


def Main_Login_2():
    """
    双账号登录
    """
    while not config.stop_thread:
        try:
            print("TASK- +++++ 主账号 开始登录 ++++++++++++++++++++++++++++++++")
            ctypes.windll.user32.SetForegroundWindow(hwnds[0])
            time.sleep(1)
            LogIn("master", hwnds[0])
            print("TASK- ----- 主账号已登录成功 --------------------------------")
        except:
            config.stop_thread = True
        break

    while not config.stop_thread:
        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "left")
        print("TASK- ----- 主窗口位置已修改 --------------------------------")
        break

    while not config.stop_thread:
        try:
            print("TASK- +++++ 从账号 开始登录 ++++++++++++++++++++++++++++++++")
            ctypes.windll.user32.SetForegroundWindow(hwnds[1])
            time.sleep(1)
            LogIn("slaves", hwnds[1])
            print("TASK- ----- 从账号已登录成功 --------------------------------")
        except:
            config.stop_thread = True
        break

    while not config.stop_thread:
        pyautogui.hotkey("win", "right")
        pyautogui.hotkey("win", "right")
        print("TASK- ----- 从窗口位置已修改 --------------------------------")

        break


def Sign_In():
    """
    邮箱奖励与庭院收菜
    """
    while not config.stop_thread:
        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[0])
        MainTask_Signin(hwnds[0])

        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[1])
        MainTask_Signin(hwnds[1])

        break


def Sis_Foster():
    """
    结界收菜种菜
    """
    while not config.stop_thread:
        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[0])
        Task_SisFoster.MainTask_Sisfoster(hwnds[0])

        print("SHIF- ^^^^^ 切换游戏账号窗口 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        ctypes.windll.user32.SetForegroundWindow(hwnds[1])
        Task_SisFoster.MainTask_Sisfoster(hwnds[1])

        break


def Full_operation():
    Main_Login_2()
    Sign_In()
    Sis_Foster()
