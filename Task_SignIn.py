import Lib
import time
import pyautogui
import ctypes
import win32gui


def LogIn(Log, Hwnd):
    """
    两个账号的登录 默认上次登录更晚的是副账号
    @return:    1正常0异常
    """

    # --------------------------------------------------------------------------------------------------------------------------------
    # region 循环判断登录界面 同时检测庭院以跳过登录

    Wait = 0
    time.sleep(3)
    while True:
        Range = Lib.Find_in_screen("./pic/Main/Jinruyouxi.png", 0.05, 0)
        if Range:
            print("检测到登录界面")
            break
        else:
            print("未检测到登录界面")
            Wait += 1

        if Wait >= 5:
            if Lib.Find_in_windows(Hwnd, "./pic/Main/Zhujiemian.png", 0.05, 0):
                print("检测到进入庭院 跳过登录")
                return 1
            else:
                print("未检测到进入庭院")

        if Wait >= 15:
            print("EROR- ***** 登录失败超时退出 ********************************")
            exit()
            break

    # endregion
    # --------------------------------------------------------------------------------------------------------------------------------
    # region 主账号登录额外的切换账号步骤

    if Log == "master":
        # 注：此处条件可以极为苛刻 一般识别取值为0.002
        Range = Lib.Find_in_screen("./pic/Main/Qiehuanzhanghao.png", 0.005, 0)
        if Range:
            Lib.Click(None, Range, 1)
            print("打开账号列表")
        else:
            print("无法打开账号列表")
            return 0

        # 注：此处条件可以极为苛刻 一般识别取值为0.000
        Range = Lib.Find_in_screen("./pic/Main/Zhuzhanghao.png", 0.005, 0)
        if Range:
            Lib.Click(None, Range, 1)
            print("选择主账号")
        else:
            print("无法识别主账号区域")
            return 0

    # endregion
    # --------------------------------------------------------------------------------------------------------------------------------
    # region 登录

    if Log == "master":
        Range = Lib.Find_in_screen("./pic/Main/Jinruyouxi0.png", 0.05, 0)
    else:
        Range = Lib.Find_in_screen("./pic/Main/Jinruyouxi.png", 0.05, 0)

    if Range:
        Lib.Click(None, Range, 2)
        print("点击账号登录")
    else:
        print("账号未登录")
        return 0

    Range = Lib.Find_in_screen("./pic/Main/Jinruyouxi1.png", 0.05, 0)
    if Range:
        Lib.Click(None, Range, 1)
        print("进入游戏")
        return 1
    else:
        print("无法进入游戏")
        return 0

    # endregion
    # --------------------------------------------------------------------------------------------------------------------------------


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
