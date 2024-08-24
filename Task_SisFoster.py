import Lib
import time
import pyautogui
import ctypes
import win32gui


def Work_Salary(Hwnd):
    """
    阴阳寮工资和体力
    :param Hwnd:    窗口句柄
    :return:        1正常0异常
    """
    # 领取阴阳寮奖励
    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jinbigongzi.png", 0.05, 0)
    if Range:
        Lib.Click(Hwnd, Range, 1)
        print("点击工资")
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Lingqu.png", 0.05, 0)
        Lib.Click(Hwnd, Range, 1)
        print("领取工资")
        Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("领取体力工资成功")
        pyautogui.press("esc")
        time.sleep(0.5)
    else:
        print("未检测到工资")

    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tiligongzi.png", 0.05, 0)
    if Range:
        Lib.Click(Hwnd, Range, 1)
        print("领取体力工资")
        Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
        print("领取体力工资成功")
        pyautogui.press("esc")
        time.sleep(0.5)
    else:
        print("未检测到体力工资")
    return 1


def Work_Foster(Hwnd):
    """
    结界寄养
    :param Hwnd:    窗口句柄
    :return:        1正常0异常
    """
    time.sleep(1)
    # 进入结界
    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiejie.png", 0.05, 0)
    if Range:
        Lib.Click(Hwnd, Range, 1)
        print("进入结界")
        time.sleep(1)
    else:
        print("未检测到结界入口")
        return 0

    def Jiyang():
        # 检测寄养奖励
        time.sleep(1)
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiyangjingyan.png", 0.05, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("检测到寄养奖励")
            time.sleep(0.5)
            Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("寄养奖励领取成功")
            pyautogui.press("esc")
            time.sleep(0.5)
        else:
            print("未检测到寄养奖励")

    def Tilishihe():
        time.sleep(1)
        # 检测体力食盒
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tilingshihe.png", 0.05, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("检测到体力食盒")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Quchu.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("取出体力食盒")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            print("体力食盒领取成功")
            pyautogui.press("esc")
            time.sleep(0.5)
            pyautogui.press("esc")
            time.sleep(0.5)
        else:
            print("未检测到体力食盒溢出")

    def Jinyanjiuhu():
        time.sleep(1)
        # 检测经验酒壶
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jingyanjiuhu.png", 0.05, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("检测到经验酒壶满")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tiqu.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("提取满的经验酒壶")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tiqu.png", 0.05, 0)
            if Range:
                pyautogui.press("esc")
                print("经验酒壶提取上限")
            else:
                print("经验酒壶提取成功")

        else:
            print("经验酒壶未满")
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jinyanjiuhu0.png", 0.05, 0)
            if Range:
                Lib.Click(Hwnd, Range, 1)
                print("检测到有经验酒壶")

                Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tiqu.png", 0.05, 0)
                Lib.Click(Hwnd, Range, 1)
                print("提取经验酒壶")

                Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tiqu.png", 0.05, 0)
                pyautogui.press("esc")
                print("经验酒壶提取上限")
            else:
                print("未检测到经验酒壶溢出")

    def Jiejiekajiangli():
        time.sleep(1)
        # 检测太鼓奖励
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiejiekajiangli.png", 0.05, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("检测到结界卡奖励 点击领取")
            time.sleep(1)

            Range = Lib.Find_in_windows(Hwnd, "./pic/Main/Huodejiangli.png", 0.05, 0)
            if not Range:
                print("寄养奖励领取成功")
            else:
                print("寄养奖励领取失败")
        else:
            print("未检测到结界卡奖励")

    def Jiejieka():
        time.sleep(1)
        # 进入结界卡界面
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiejieka.png", 0.07, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("进入结界卡界面")
            time.sleep(1)
        else:
            print("未进入结界卡界面")
            return 0

        time.sleep(1)
        # 放置结界卡
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiejiekacao.png", 0.05, 0)
        if not Range:
            print("结界卡未耗尽")
            pyautogui.press("esc")
            time.sleep(0.5)
        else:
            print("结界卡已经耗尽")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiejiekaliebiao.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("打开结界卡列表")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Taiguliebiao.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击太鼓")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Xingjijiangxu.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击星级降序")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Shouzhangjiejieka.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击首张结界卡")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jihuo.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击激活")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Yaoqing.png", 0.05, 0)
            if Range:
                print("结界卡激活成功")
                time.sleep(1)
                pyautogui.press("esc")
                time.sleep(0.5)
            else:
                print("结界卡激活失败")
                return 0

    def Yucheng():
        time.sleep(1)
        # 进入结界育成
        Wait = 0
        while True:
            time.sleep(0.5)
            # 检测到进入结界育成界面 退出循环
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Shishenyucheng.png", 0.05, 0)
            if Range:
                Lib.Click(Hwnd, Range, 1)
                print("检测到进入结界育成界面")
                break

            Wait += 1
            time.sleep(1)
            print("未检测到进入结界育成界面")

            # 10s未检测到 超时退出
            if Wait >= 10:
                Wait = 0
                print("EROR- XXXXX 结界育成 超时退出 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                return 0

        # 检测是否有满级式神
        while True:
            time.sleep(0.5)
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Manjidamo.png", 0.05, 0)
            if Range:
                Lib.Click(Hwnd, Range, 1)
                print("检测到有满级式神")
            else:
                print("未检测到有满级式神")
                break

        # 进入素材列表
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Quanbu.png", 0.05, 0)
        Lib.Click(Hwnd, Range, 1)
        print("进入式神列表")

        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Sucai.png", 0.05, 0)
        Lib.Click(Hwnd, Range, 1)
        print("选择素材")

        while True:
            time.sleep(0.5)
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Fangrushishen.png", 0.05, 0)
            if Range:
                print("检测到有空位")

                Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Fengweidamo.png", 0.05, 0)
                if Range:
                    Lib.Click(Hwnd, Range, 1)
                    print("放上去一个奉为达摩")
                else:
                    print("未检测到达摩素材")
                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Yuchengliebioakuang.png", 0.05, 0)

                    print("进入翻页区域")
                    rect = win32gui.GetWindowRect(Hwnd)
                    x = (Range[0][0] + Range[1][0]) // 2 + rect[0]
                    y = (Range[0][1] + Range[1][1]) // 2 + rect[1]
                    pyautogui.moveTo(x, y)

                    pyautogui.scroll(-200)
                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Fengweidamo.png", 0.05, 0)

                    if Range:
                        Lib.Click(Hwnd, Range, 1)
                        print("放上去一个奉为达摩")
                    else:
                        print("查找奉为达摩失败")
            else:
                print("育成池已经放满")
                break

        # 寄养
        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiyangrukou.png", 0.05, 0)
        if Range:
            Lib.Click(Hwnd, Range, 1)
            print("检测到寄养空位")
        else:
            print("未检测到寄养空位")
            pyautogui.press("esc")
            time.sleep(3)
            return 1

        def Jiyang(Jiejieka_Model_path, string):
            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Kuaqu.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击跨区")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Haoyou.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击好友")

            Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiyangliebiao.png", 0.05, 0)
            Lib.Click(Hwnd, Range, 1)
            print("点击寄养列表")

            while True:
                time.sleep(0.5)
                Range = Lib.Find_in_windows(Hwnd, Jiejieka_Model_path, 0.05, 0)
                if Range:
                    Lib.Click(Hwnd, Range, 1)
                    print("检测到", end="")
                    print(string)

                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jinrujiejie.png", 0.05, 0)
                    Lib.Click(Hwnd, Range, 2)
                    print("点击进入结界")

                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Quanbu.png", 0.05, 0)
                    Lib.Click(Hwnd, Range, 1)
                    print("进入式神列表")

                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Sucai.png", 0.05, 0)
                    Lib.Click(Hwnd, Range, 1)
                    print("选择素材")

                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Fengweidamo.png", 0.05, 0)
                    if Range:
                        Lib.Click(Hwnd, Range, 1)
                        print("放上去一个奉为达摩")
                    else:
                        pyautogui.scroll(-100)
                        Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Fengweidamo.png", 0.05, 0)
                        Lib.Click(Hwnd, Range, 2)
                        print("放上去一个奉为达摩")

                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Queding.png", 0.05, 0)
                    Lib.Click(Hwnd, Range, 1)
                    print("点击确定")
                    pyautogui.press("esc")
                    time.sleep(2)
                    pyautogui.press("esc")
                    time.sleep(2)
                    return 0
                else:
                    print("未检测到", end="")
                    print(string)
                    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Jiyangliebiaomowei.png", 0.001, 0)

                    if Range:
                        print("已经到寄养列表末尾")
                        return 1
                    else:
                        pyautogui.scroll(-400)
                        print("往下翻页")

        flag_Jiyang = Jiyang("./pic/Sis/6xingtaigu.png", "六星太鼓")
        if flag_Jiyang:
            flag_Jiyang = Jiyang("./pic/Sis/6xingdouyu.png", "六星斗鱼")
            if flag_Jiyang:
                flag_Jiyang = Jiyang("./pic/Sis/5xingtaigu.png", "五星太鼓")
                if flag_Jiyang:
                    flag_Jiyang = Jiyang("./pic/Sis/5xingdouyu.png", "六星斗鱼")
                    if flag_Jiyang:
                        return 1
        ##

    Jiyang()
    Jiejiekajiangli()
    Yucheng()
    Tilishihe()
    Jinyanjiuhu()
    Jiejieka()
    Yucheng()

    # 回到寮界面
    pyautogui.press("esc")
    time.sleep(2)

    Range = Lib.Find_in_windows(Hwnd, "./pic/Sis/Tuichu.png", 0.05, 0)
    Lib.Click(Hwnd, Range, 1)
    print("退出寮界面")

    return 1


def MainTask_Sisfoster(Hwnd):
    """
    有关结界寄养相关任务
    :param Hwnd:    窗口句柄
    """
    # 先进入阴阳寮界面
    Lib.Itface_guild(Hwnd)

    # 开始领取工资任务
    print("TASK- +++++ 开始领取工资任务 ++++++++++++++++++++++++++++++++")
    time.sleep(0.5)
    if Work_Salary(Hwnd):
        print("TASK- ----- 领取工资任务完成 --------------------------------")
    else:
        print("EROR- XXXXX 领取工资任务失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # 开始结界寄养任务
    print("TASK- +++++ 开始结界寄养任务 ++++++++++++++++++++++++++++++++")
    time.sleep(0.5)
    if Work_Foster(Hwnd):
        print("TASK- ----- 结界寄养任务完成 --------------------------------")
    else:
        print("EROR- XXXXX 结界寄养任务失败 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
