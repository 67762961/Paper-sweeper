import time
import pyautogui
import ctypes
import win32gui
from Lib import Find_in_windows, Find_Click_windows, Click, Itface_Host


def Work_Mail(Hwnd):
    """
    领取邮件奖励
    @param Hwnd:    窗口句柄
    @return:        1为正常 0为异常
    """
    Find_Click_windows(Hwnd, "./pic/Mail/Youjian.png", 0.05, "点击邮件", "未识别到邮件入口")

    # 检测邮箱界面
    if Find_in_windows(Hwnd, "./pic/Mail/Youxiang.png", 0.1, 0):
        print("检测到进入邮箱")
    else:
        print("进入邮箱异常")
        time.sleep(0.5)
        return 0

    # 检测是否有奖励未领取
    Range = Find_in_windows(Hwnd, "./pic/Mail/Quanbulingqu.png", 0.05, 0)

    # 没有奖励未领取 检测消息邮件 然后返回
    if not Range:
        print("没有奖励未领取")
        # 检测消息邮件
        while 1:
            if not Find_Click_windows(Hwnd, "./pic/Mail/Xiaoxiyoujian.png", 0.05, "发现消息邮件", "未发现消息邮件"):
                break
        pyautogui.press("esc")
        time.sleep(0.5)
        return 1

    # 有奖励未领取
    else:
        print("有奖励未领取")
        # 点击全部领取
        Click(Hwnd, Range, 1)

        # 检测全部领取界面
        if Find_in_windows(Hwnd, "./pic/Mail/Quanbulingqujiemian.png", 0.05, 0):
            print("检测到进入领取界面")
        else:
            print("error 未正常领取")
            time.sleep(0.5)
            return 0

        # 点击确定
        Find_Click_windows(Hwnd, "./pic/Main/Queding.png", 0.05, "点击确定", "未正常领取确认")

        # 检测领取
        if Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0):
            print("领取成功")
            # 按下esc退出
            pyautogui.press("esc")
            time.sleep(0.5)
            # 检测消息邮件
            while 1:
                if not Find_Click_windows(Hwnd, "./pic/Mail/Xiaoxiyoujian.png", 0.05, "点击消息邮件", "未发现消息邮件"):
                    break
            pyautogui.press("esc")
            time.sleep(0.5)
            return 1


def Work_Sign(Hwnd):
    """
    签到以及领取每日福袋
    @param Hwnd:    窗口句柄
    """

    Itface_Host(Hwnd)
    Flag_fudai = 0

    # 检测福袋小纸人
    if not Flag_fudai:
        if Find_Click_windows(Hwnd, "./pic/Sign/Fudaixiaozhiren.png", 0.05, "检测到福袋小纸人", "未检测到福袋小纸人"):
            # 点击福袋小人后检测领取状态
            Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("福袋领取成功")
            Flag_fudai = 1
            pyautogui.press("esc")
            time.sleep(0.5)
    #######################################################################################
    Wait = 0
    while True:
        # 检测签到小纸人
        Range = Find_in_windows(Hwnd, "./pic/Sign/Qiandaoxiaozhiren.png", 0.05, 0)
        if not Range:
            print("未检测到签到小纸人")
            time.sleep(0.5)
            Wait += 1
            if Wait >= 3:
                break
        else:
            print("检测到签到小纸人")
            Click(Hwnd, Range, 1)
            Range = Find_in_windows(Hwnd, "./pic/Sign/Meiriyiqian.png", 0.05, 0)
            print("每日一签")
            Click(Hwnd, Range, 2)
            Range = Find_in_windows(Hwnd, "./pic/Sign/Jieqianxiaozhiren.png", 0.05, 0)
            print("每日一签成功")
            pyautogui.press("esc")
            time.sleep(0.01)
            break

    Itface_Host(Hwnd)

    if not Flag_fudai:
        Range = Find_in_windows(Hwnd, "./pic/Sign/Fudaixiaozhiren.png", 0.05, 0)
        if not Range:
            print("未检测到福袋小纸人")
        else:
            print("检测到福袋小纸人")
            Click(Hwnd, Range, 1)
            Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("福袋领取成功")
            Flag_fudai = 1
            pyautogui.press("esc")
            time.sleep(0.5)

    Itface_Host(Hwnd)

    # 检测体力小纸人
    Range = Find_in_windows(Hwnd, "./pic/Sign/Tilixiaozhire.png", 0.05, 0)
    if not Range:
        print("未检测到体力小纸人")
    else:
        print("检测到体力小纸人")
        Click(Hwnd, Range, 1)
        Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("体力领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)

    Itface_Host(Hwnd)

    # 检测勾玉小纸人
    Range = Find_in_windows(Hwnd, "./pic/Sign/Gouyuxiaozhiren.png", 0.05, 0)
    if not Range:
        print("未检测到勾玉小纸人")
    else:
        print("检测到勾玉小纸人")
        Click(Hwnd, Range, 1)
        Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("勾玉领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)

    Itface_Host(Hwnd)

    # 检测buff小纸人
    Range = Find_in_windows(Hwnd, "./pic/Sign/BUFFxiaozhiren.png", 0.05, 0)
    if not Range:
        print("未检测到BUFF小纸人")
    else:
        print("检测到BUFF小纸人")
        Click(Hwnd, Range, 1)
        Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("BUFF领取成功")
        pyautogui.press("esc")
        time.sleep(0.5)


def MainTask_Signin(Hwnd):
    """
    完成每日登录所有领取项
    @param Hwnd:    窗口句柄
    """

    # 检测是否位于庭院主界面
    Itface_Host(Hwnd)

    # 开始领取邮件奖励
    print("TASK- +++++ 开始领取邮件奖励 ++++++++++++++++++++++++++++++++")
    time.sleep(0.5)
    if Work_Mail(Hwnd):
        print("TASK- ----- 邮件奖励领取成功 --------------------------------")
    else:
        print("EROR- ***** 邮件奖励领取失败 ********************************")

    # 检测是否位于庭院主界面
    Itface_Host(Hwnd)

    # 开始每日签到以及福袋领取
    print("TASK- +++++ 开始领取签到奖励 ++++++++++++++++++++++++++++++++")
    Work_Sign(Hwnd)
    print("TASK- ----- 领取签到奖励成功 --------------------------------")
