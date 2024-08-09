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


def init():
    """
    提升管理员权限 获取窗口句柄 并分别登录账号
    """
    global hwnds
    user32 = ctypes.windll.user32

    # --------------------------------------------------------------------------------------------------------------------------------
    # region 提升管理员权限 并获取游戏窗口句柄

    # 检测是否管理员用户
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # 请求提升权限
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit(0)

    # 首先获取游戏窗口句柄列表
    hwnds = Lib.Find_windows("阴阳师-网易游戏")
    if len(hwnds) == 2:
        print("INIT- ····· 已经获取到两个游戏窗口")
    else:
        print("EROR- ***** 未找到 两个窗口 ********************************")
        sys.exit()

    # endregion
    # --------------------------------------------------------------------------------------------------------------------------------
    # region 分别登录账号

    # 将第一个窗口设定为前台窗口 并登录主账号
    ctypes.windll.user32.SetForegroundWindow(hwnds[0])
    log = Task_SignIn.LogIn("master", hwnds[0])
    Task_SignIn.WindowMov("master", hwnds[0])
    if not log:
        print("EROR- ***** 主账号 登录失败 ********************************")
        sys.exit()

    # 将第二个窗口设定为前台窗口 并登录从账号
    ctypes.windll.user32.SetForegroundWindow(hwnds[1])
    log = Task_SignIn.LogIn("slave", hwnds[1])
    Task_SignIn.WindowMov("slave", hwnds[1])
    if not log:
        print("EROR- ***** 从账号 登录失败 ********************************")
        sys.exit()
    # endregion
    # --------------------------------------------------------------------------------------------------------------------------------


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


init()
Sign_In()
Sis_Foster()
