import Lib
import pyautogui
import ctypes
import win32gui
import config
from time import sleep
from datetime import datetime, timedelta, time
from Lib import Find_in_windows, Find_Click_windows, Click, Itface_Host, Itface_guild, read_config, write_config


def meirifengmo(Hwnd):
    # 点四下逢魔
    while True:
        Range = Find_in_windows(Hwnd, "./pic/Fengmo/Fengmocishu.png", 0.03, 0)
        if Range:
            print("还有逢魔次数")
            Find_Click_windows(Hwnd, "./pic/Fengmo/Xianshifengmo.png", 0.05, "点击现世逢魔", "未检测到现世逢魔图标")
            sleep(2.5)
        else:
            print("逢魔次数耗尽")
            break

    # 领取逢魔奖励
    for i in range(3):
        flag = Find_Click_windows(Hwnd, "./pic/Fengmo/Fengmojiangli.png", 0.05, "点击逢魔奖励", "未检测到现世逢魔奖励")
        if flag:
            if Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0):
                print("逢魔奖励领取成功")
                pyautogui.press("esc")
                break
            else:
                print("逢魔奖励领取失败")
        else:
            if Find_in_windows(Hwnd, "./pic/Fengmo/Fengmojiangliyilingqu.png", 0.05, 0):
                print("逢魔奖励已经被领取")
                break
            else:
                print("逢魔奖励未正确领取")


def fengmoboss(Hwnd):
    """
    封魔打boss
    """
    # 初始化
    sleep(1)
    flag_boss = 1
    flag_Ji = True
    found_battle_scene = False
    Find_Click_windows(Hwnd, "./pic/Fengmo/Dingwei.png", 0.05, "点击定位", "未检测到定位图标")

    # 找boss循环
    for p in range(4):
        for i in range(2):
            # 优先打逢魔-极
            if flag_Ji:
                Range = Find_Click_windows(Hwnd, "./pic/Fengmo/Fengmoji.png", 0.05, "点击逢魔-极", "未检测到逢魔-极图标")
                if Range:
                    flag_boss = 1
                    sleep(1)
                    break
            else:
                # 封魔-极检索失败则转为打首领
                if Find_Click_windows(Hwnd, "./pic/Fengmo/Shouling.png", 0.05, "点击首领", "未检测到首领图标"):
                    flag_boss = 0
                    sleep(1)
                    break

        # 集结 简化为只识别一次
        for i in range(1):
            if flag_boss:
                Range = Find_Click_windows(Hwnd, "./pic/Fengmo/Jijie.png", 0.05, "点击集结", "未检测到集结图标")
            else:
                Range = Find_Click_windows(Hwnd, "./pic/Fengmo/Jijie0.png", 0.05, "点击集结", "未检测到集结图标")

            sleep(1)

            if Range:
                if flag_boss:
                    Find_Click_windows(Hwnd, "./pic/Fengmo/Jijietioazhan.png", 0.05, "点击集结挑战", "未检测到集结挑战")
                else:
                    Find_Click_windows(Hwnd, "./pic/Fengmo/Jijietioazhan1.png", 0.05, "点击集结挑战", "未检测到集结挑战")
                if Find_in_windows(Hwnd, "./pic/Fengmo/Zhengrongyushe.png", 0.05, 0):
                    print("已经进入备战场景")
                    found_battle_scene = True
                    break
                else:
                    print("未进入备战场景")
            # 在备战场景就退出循环
            if found_battle_scene:
                break

        # 三次寻找封魔-极无果就改换首领
        if p == 2:
            flag_Ji = False

        # 在备战场景就退出循环
        if found_battle_scene:
            break

    # 此处进入了打boss场景 应添加后续战斗完成的处理


def MainTask_Fengmo(Hwnd, Account):
    """
    有关逢魔之时相关任务
    :param Hwnd:    窗口句柄
    :param Account: 账号
    """
    print("TASK- +++++ 开始逢魔之时任务 ++++++++++++++++++++++++++++++++")

    # 读取上次封魔之时执行时间
    config = read_config("./config/Last_times.json")
    Times_fengmozhishi_str = config[Account].get("Times_fengmozhishi", None)
    Times_fengmozhishi = datetime.fromisoformat(Times_fengmozhishi_str) if Times_fengmozhishi_str else None
    current_time = datetime.now()
    if Times_fengmozhishi is not None:
        print(f"TIME- ----- 上次逢魔之时时间: {Times_fengmozhishi.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("TIME- ----- 没有记录上次逢魔之时时间")
        one_week_ago = current_time - timedelta(weeks=1)
        config[Account]["Times_fengmozhishi"] = one_week_ago.isoformat()
        write_config("./config/Last_times.json", config)

    # 开启条件
    flag_fengmo = time(17, 0) <= current_time.time() <= time(22, 0)
    if (Times_fengmozhishi.date() != current_time.date()) & flag_fengmo:

        # 开始逢魔任务
        print("INFO- ----- 前往逢魔界面")
        # ##########################################################################################################
        # 此处有多个日常入口
        Find_Click_windows(Hwnd, "./pic/Main/Fengmorukou.png", 0.05, "进入逢魔入口", "未检测到逢魔入口")
        Find_Click_windows(Hwnd, "./pic/Main/Yinjiezhimenrukou.png", 0.05, "进入阴界之门入口", "未检测到阴界之门入口")

        Range = Find_Click_windows(Hwnd, "./pic/Fengmo/Fengmotubiao.png", 0.05, "点击逢魔图标", "未检测到逢魔图标")
        if not Range:
            print("EROR- XXXXX 逢魔之时任务失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            return 0
        else:
            if Find_Click_windows(Hwnd, "./pic/Main/Qianwang.png", 0.05, "点击前往", "未检测到前往图标"):
                sleep(2)
                # 先点封魔再打boss
                meirifengmo(Hwnd)
                fengmoboss(Hwnd)
    else:
        print("SKIP- ----- 跳过逢魔之时")
