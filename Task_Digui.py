import Lib
import pyautogui
import ctypes
import win32gui
import config
from time import sleep
from datetime import datetime, timedelta, time
from Lib import Find_in_windows, Find_Click_windows, Click, Itface_Host, Itface_guild, Itface_explore, read_config, write_config, check_lasttime


def MainTask_Digui(Hwnd, Account):
    """
    有关地鬼相关任务
    :param Hwnd:    窗口句柄
    :param Account: 账号
    """
    print("TASK- +++++ 开始讨伐地域鬼王 ++++++++++++++++++++++++++++++++")

    # 读取上次地鬼执行时间
    Times_diyuguiwang = check_lasttime(Account, "Times_diyuguiwang")
    current_time = datetime.now()

    # 判断跳过条件
    if Times_diyuguiwang.date() == current_time.date():
        print("SKIP- ----- 跳过地鬼任务")
    else:
        # 开始地鬼任务
        print("INFO- ----- 前往地鬼界面")
        Itface_explore(Hwnd)

        ##################################
        # pyautogui.press("esc")


######################################################################################################################

# # 更新配置，写入当前时间
# config = read_config("./config/Last_times.json")
# Now = current_time.strftime("%Y-%m-%d %H:%M:%S")
# config[Account]["Times_diyuguiwang"] = Now
# print("TIME- ----- 本次逢魔之时完成时间")
# print(f"TIME- ----- {Now}")
# write_config("./config/Last_times.json", config)
# break
