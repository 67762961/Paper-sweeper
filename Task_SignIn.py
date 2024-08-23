import Lib
import time
import pyautogui
import ctypes
import win32gui


def Work_Mail(Hwnd):
    """
    领取邮件奖励
    @param Hwnd:    窗口句柄
    @return:        1为正常 0为异常
    """
    # 点击邮件
    Range = Lib.Find_in_windows(Hwnd, "./pic/Mail/Youjian.png", 0.05, 0)
    if Range:
        print("点击邮件")
        Lib.Click(Hwnd, Range, 1)
    else:
        print("未识别到邮件入口")
        return 0

    # 检测邮箱界面
    if Lib.Find_in_windows(Hwnd, "./pic/Mail/Youxiang.png", 0.1, 0):
        Itface = "Mail"
        print("检测到进入邮箱")
    else:
        print("error 进入邮箱异常")
        time.sleep(0.5)
        return 0

    # 检测是否有奖励未领取
    Range = Lib.Find_in_windows(Hwnd, "./pic/Mail/Quanbulingqu.png", 0.05, 0)

    # 没有奖励未领取 检测消息邮件 然后返回
    if not Range:
        print("没有奖励未领取")
        # 检测消息邮件
        while 1:
            Range = Lib.Find_in_windows(Hwnd, "./pic/Mail/Xiaoxiyoujian.png", 0.05, 0)
            if Range:
                print("发现消息邮件")
                Lib.Click(Hwnd, Range, 1)
            else:
                print("未发现消息邮件")
                break
        pyautogui.press("esc")
        return 1

    # 有奖励未领取
    else:
        print("有奖励未领取")
        # 点击全部领取
        Lib.Click(Hwnd, Range, 1)

        # 检测全部领取界面
        if Lib.Find_in_windows(Hwnd, "./pic/Mail/Quanbulingqujiemian.png", 0.05, 0):
            Itface = "Mail"
            print("检测到进入领取界面")
        else:
            print("error 未正常领取")
            time.sleep(0.5)
            return 0

        # 点击确定
        Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Queding.png", 0.05, 0)
        if Range:
            print("点击确定")
            Lib.Click(Hwnd, Range, 1)
        else:
            print("error 未正常领取确认")
            time.sleep(0.5)
            return 0

        # 检测领取
        if Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0):
            print("领取成功")
            # 按下esc退出
            pyautogui.press("esc")
            time.sleep(0.5)
            # 检测消息邮件
            while 1:
                Range = Lib.Find_in_windows(
                    Hwnd, "./pic/Mail/Xiaoxiyoujian.png", 0.05, 0
                )
                if Range:
                    print("发现消息邮件")
                    Lib.Click(Hwnd, Range, 1)
                else:
                    print("未发现消息邮件")
                    break
            pyautogui.press("esc")
            time.sleep(0.5)
            return 1


def Work_Sign(Hwnd):
    """
    签到以及领取每日福袋
    @param Hwnd:    窗口句柄
    """

    Lib.Itface_Host(Hwnd)
    Flag_fudai = 0

    Lib.Itface_Host(Hwnd)

    # 检测福袋小纸人
    if not Flag_fudai:
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Fudaixiaozhiren.png", 0.05, 0)
        if not Range:
            print("未检测到福袋小纸人")
        else:
            print("检测到福袋小纸人")
            Lib.Click(Hwnd, Range, 1)
            Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("福袋领取成功")
            Flag_fudai = 1
            pyautogui.press("esc")
            time.sleep(0.5)

    Wait = 0
    while True:
        # 检测签到小纸人
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Qiandaoxiaozhiren.png", 0.05, 0)
        if not Range:
            print("未检测到签到小纸人")
            time.sleep(0.5)
            Wait += 1
            if Wait >= 3:
                break
        else:
            print("检测到签到小纸人")
            Lib.Click(Hwnd, Range, 1)
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Meiriyiqian.png", 0.05, 0)
            print("每日一签")
            Lib.Click(Hwnd, Range, 2)
            Range = Lib.Find_in_windows(
                Hwnd, "./pic/Sign/Jieqianxiaozhiren.png", 0.05, 0
            )
            print("每日一签成功")
            pyautogui.press("esc")
            time.sleep(0.01)
            break

    Lib.Itface_Host(Hwnd)

    if not Flag_fudai:
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Fudaixiaozhiren.png", 0.05, 0)
        if not Range:
            print("未检测到福袋小纸人")
        else:
            print("检测到福袋小纸人")
            Lib.Click(Hwnd, Range, 1)
            Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("福袋领取成功")
            Flag_fudai = 1
            pyautogui.press("esc")
            time.sleep(0.5)

    Lib.Itface_Host(Hwnd)

    # 检测体力小纸人
    Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Tilixiaozhire.png", 0.05, 0)
    if not Range:
        print("未检测到体力小纸人")
    else:
        print("检测到体力小纸人")
        Lib.Click(Hwnd, Range, 1)
        Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("体力领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)

    Lib.Itface_Host(Hwnd)

    # 检测勾玉小纸人
    Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/Gouyuxiaozhiren.png", 0.05, 0)
    if not Range:
        print("未检测到勾玉小纸人")
    else:
        print("检测到勾玉小纸人")
        Lib.Click(Hwnd, Range, 1)
        Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("勾玉领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)

    Lib.Itface_Host(Hwnd)

    # 检测buff小纸人
    Range = Lib.Find_in_windows(Hwnd, "./pic/Sign/BUFFxiaozhiren.png", 0.05, 0)
    if not Range:
        print("未检测到BUFF小纸人")
    else:
        print("检测到BUFF小纸人")
        Lib.Click(Hwnd, Range, 1)
        Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("BUFF领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)


def MainTask_Signin(Hwnd):
    """
    完成每日登录所有领取项
    :param Hwnd:    窗口句柄
    """

    # 检测是否位于庭院主界面
    Itface = 0
    Lib.Itface_Host(Hwnd)

    # 开始领取邮件奖励
    print("TASK- +++++ 开始领取邮件奖励 ++++++++++++++++++++++++++++++++")
    time.sleep(0.5)
    if Work_Mail(Hwnd):
        print("TASK- ----- 邮件奖励领取成功 --------------------------------")
    else:
        print("EROR- ***** 邮件奖励领取失败 ********************************")

    # 检测是否位于庭院主界面
    Lib.Itface_Host(Hwnd)

    # 开始每日签到以及福袋领取
    print("TASK- +++++ 开始领取签到奖励 ++++++++++++++++++++++++++++++++")
    Work_Sign(Hwnd)
    print("TASK- ----- 领取签到奖励成功 --------------------------------")
