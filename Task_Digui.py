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
    # 当日未执行过 且现在时间在12点到23:50之间
    if Times_diyuguiwang.date() == current_time.date() or (not (time(12, 0) <= current_time.time() <= time(23, 50))):
        print("SKIP- ----- 跳过地鬼任务")
    else:
        # 开始地鬼任务
        print("INFO- ----- 前往地鬼界面")
        Itface_explore(Hwnd)
        if Diyuguiwang("探索界面", Hwnd):
            # 更新配置 写入当前时间
            config = read_config("./config/Last_times.json")
            Now = current_time.strftime("%Y-%m-%d %H:%M:%S")
            config[Account]["Times_diyuguiwang"] = Now
            print("TIME- ----- 本次地域鬼王完成时间")
            print(f"TIME- ----- {Now}")
            write_config("./config/Last_times.json", config)
            print("TASK- ----- 地域鬼王任务完成 --------------------------------")
        else:
            print("EROR- ***** 地域鬼王任务失败 ********************************")


def Diyuguiwang(current_state, Hwnd):
    """
    挑战地域鬼王
    """
    # 地鬼计数器
    flag_digui = 1
    print("STEP- vvvvv 从{First_state}开始".format(First_state=current_state))
    for step in range(30):
        sleep(1)
        match current_state:
            case "探索界面":
                Find = Find_Click_windows(Hwnd, "./pic/Digui/Diguitubiao.png", 0.05, "进入地鬼界面", "未检测到地鬼图标")
                if Find:
                    print("STEP- vvvvv 跳转地鬼界面")
                    current_state = "地鬼界面"
                else:
                    print("STEP- vvvvv 跳转异常退出界面")
                    current_state = "异常退出"

            case "地鬼界面":
                sleep(1)
                if flag_digui <= 3:
                    Find = Find_Click_windows(Hwnd, "./pic/Digui/Shaixuan.png", 0.05, "点击筛选", "未检测到筛选图标")
                    if Find:
                        print("STEP- vvvvv 跳转筛选界面")
                        current_state = "筛选界面"
                    else:
                        print("STEP- vvvvv 跳转异常退出界面")
                        current_state = "异常退出"
                else:
                    print("STEP- vvvvv 跳转结束状态")
                    current_state = "结束"

            case "筛选界面":
                Find_Click_windows(Hwnd, "./pic/Digui/Remen.png", 0.01, "点击热门", "似乎已经在热门选项中")
                sleep(1)
                match flag_digui:
                    case 1:
                        Find = Find_Click_windows(Hwnd, "./pic/Digui/1st.png", 0.05, "点击第一个", "似乎无法挑战第一热门鬼王")
                    case 2:
                        Find = Find_Click_windows(Hwnd, "./pic/Digui/2nd.png", 0.05, "点击第二个", "似乎无法挑战第二热门鬼王")
                    case 3:
                        Find = Find_Click_windows(Hwnd, "./pic/Digui/3rd.png", 0.05, "点击第三个", "似乎无法挑战第三热门鬼王")

                sleep(1)
                if Find_in_windows(Hwnd, "./pic/Digui/Zuixin.png", 0.01, 0):
                    print("检测到最新栏 似乎无法挑战热门")
                    Find_Click_windows(Hwnd, "./pic/Digui/Zuixin.png", 0.01, "点击最新", "点击最新失败")
                    Find = Find_Click_windows(Hwnd, "./pic/Digui/Zuixintiaozhan.png", 0.03, "点击最新挑战", "未检测到最新挑战图标")
                    if Find:
                        print("STEP- vvvvv 跳转挑战界面")
                        current_state = "挑战界面"
                    else:
                        print("STEP- vvvvv 似乎已经无挑战次数 跳转结束")
                        sleep(1)
                        pyautogui.press("esc")
                        sleep(1)
                        current_state = "结束"
                else:
                    print("未检测到最新栏 似乎可以挑战热门")
                    if Find:
                        print("STEP- vvvvv 跳转挑战界面")
                        current_state = "挑战界面"
                    else:
                        print("STEP- vvvvv 跳转异常退出界面")
                        current_state = "异常退出"

            case "挑战界面":
                sleep(1)
                Find = Find_Click_windows(Hwnd, "./pic/Digui/Tiaozhan.png", 0.05, "点击开始挑战", "未检测到挑战图标")
                if Find:
                    print("STEP- vvvvv 跳转战斗准备阶段")
                    current_state = "战斗准备阶段"
                else:
                    print("STEP- vvvvv 跳转异常退出界面")
                    current_state = "异常退出"

            case "战斗准备阶段":
                sleep(1)
                for Wait in range(10):
                    Find = Find_Click_windows(Hwnd, "./pic/Digui/Zhunbei.png", 0.07, "点击准备", "未检测到准备图标")
                    if Find:
                        print("STEP- vvvvv 跳转战斗阶段")
                        current_state = "战斗阶段"
                        break
                    else:
                        print("WAIT- wwwww 等待准备 已等待 {waittime} 秒".format(waittime=Wait + 1))
                        sleep(1)
                if not Find:
                    print("STEP- vvvvv 跳转异常退出界面")
                    current_state = "异常退出"

            case "战斗阶段":
                sleep(10)
                for Wait in range(60):
                    if Find_Click_windows(Hwnd, "./pic/Digui/Shengli.png", 0.05, "点击胜利", "似乎战斗未结束"):
                        sleep(1)
                        Find = Find_Click_windows(Hwnd, "./pic/Digui/Zhandoujiangli.png", 0.05, "点击战斗奖励", "未检测到战斗奖励图标")
                        if Find:
                            flag_digui += 1
                            sleep(1)
                            pyautogui.press("esc")
                            print("STEP- vvvvv 跳转地鬼界面")
                            current_state = "地鬼界面"
                        else:
                            print("STEP- vvvvv 跳转异常退出界面")
                            current_state = "异常退出"
                        break
                    else:
                        print("WAIT- wwwww 等待战斗 已等待 {waittime} 秒".format(waittime=Wait * 5 + 10))
                        sleep(5)

            case "结束":
                Find_Click_windows(Hwnd, "./pic/Digui/Jinritioazhan.png", 0.05, "点击今日挑战", "未检测到今日挑战图标")
                if Find_in_windows(Hwnd, "./pic/Digui/Weixuanze.png", 0.05, 0):
                    print("发现仍然有鬼王挑战次数 继续讨伐地域鬼王")
                    return Diyuguiwang("地鬼界面", Hwnd)
                else:
                    print("似乎已无地域鬼王讨伐次数 任务结束")
                    # 任务结束
                    sleep(2)
                    pyautogui.press("esc")
                    sleep(2)
                    pyautogui.press("esc")
                    sleep(2)
                    Itface_Host(Hwnd)
                    return 1

            case "异常退出":
                # 错误结束
                Itface_Host(Hwnd)
                return 0
