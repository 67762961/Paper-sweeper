import win32gui
import win32api
import win32ui
import win32con
import win32process
import ctypes
import cv2
import pyautogui
import pydirectinput
import time
import numpy as np
import random
from enum import Enum
from PIL import ImageGrab
from datetime import datetime
import os
import sys
import config
import json


def Sleep_print(Wait_time):
    time.sleep(Wait_time)
    print("WAIT- sssss 等待{Time}秒钟".format(Time=Wait_time))


def Scroll_print(length):
    for i in range(abs(length)):
        pyautogui.scroll(int(length / abs(length)))
        time.sleep(0.01)
    print("Move- mmmmm 滚轮滚动{Length}".format(Length=length))


def Esc_print():
    pydirectinput.press("esc")
    time.sleep(0.1)
    print("QUIT- ccccc 按Esc退出")


def Find_windows(title):
    """
    寻找与标题相符的句柄
    :param title:   窗口标题
    :return:        返回符合的窗口列表
    """

    # 枚举窗口
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and title in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def Find_in_windows(Hwnd, Model_path, Threshold, Flag_show):
    """
    全屏截图 找到与模板匹配的图片区域
    :param Hwnd:            窗口句柄
    :param Model_path:      用来检测的模板图片的路径
    :param Threshold:       匹配的方差阈值 越小越好
    :param Flag_show:       是否输出框选后图片 1为输出
    :return:                返回检测到的区域范围坐标左上和右下
    """

    # 获取窗口位置和大小（考虑 DPI 缩放）
    window_rect = win32gui.GetWindowRect(Hwnd)
    left, top, right, bottom = window_rect

    # 获取DPI缩放因子
    # dpi_scale = win32api.GetDeviceCaps(win32api.GetDC(Hwnd), win32con.LOGPIXELSX) / 96.0
    # 此处因为不明原因无法获取 1K分辨路下默认缩放为0.5
    # dpi_scale = 0.5
    dpi_scale = 1

    # 计算实际截图大小，考虑DPI缩放
    width = int((right - left) * dpi_scale)
    height = int((bottom - top) * dpi_scale)

    # 使用BitBlt截取窗口图像
    hdc_window = win32gui.GetWindowDC(Hwnd)
    hdc_mfc = win32ui.CreateDCFromHandle(hdc_window)
    memdc = hdc_mfc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(hdc_mfc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), hdc_mfc, (0, 0), win32con.SRCCOPY)

    # 将截图数据转换为OpenCV可以处理的格式
    bmp_info = bmp.GetInfo()
    bmp_str = bmp.GetBitmapBits(True)
    screenshot = np.frombuffer(bmp_str, dtype=np.uint8).reshape((height, width, 4))

    # 将RGBA格式的 screenshot 转换为RGB格式
    Img = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2RGB)

    # 根据DPI缩放因子调整图像大小
    Img = cv2.resize(Img, (int(width / dpi_scale), int(height / dpi_scale)))

    # 加载图像模板 并读取宽高
    Img_model = cv2.imread(Model_path)
    if Img_model is None:
        raise ValueError(f"无法找到文件: {Img_model_path}")
    Img_model_height, Img_model_width = Img_model.shape[0:2]

    # 确保 Img 和 Img_model 的数据类型为 np.uint8
    Img = np.uint8(Img)
    Img_model = np.uint8(Img_model)

    # 进行模板匹配 归一化平方差匹配方法 越小越好
    Result = cv2.matchTemplate(Img, Img_model, cv2.TM_SQDIFF_NORMED)

    # 获取匹配结果中的最大值、最小值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Result)

    # 确定识别到的区域
    Left_up = min_loc
    Right_down = (min_loc[0] + Img_model_width, min_loc[1] + Img_model_height)

    if Flag_show:
        # 在图像上绘制边框，并显示截取窗口部分的图像
        cv2.rectangle(Img, Left_up, Right_down, (0, 0, 255), 2)

        # 显示标记后的图像
        cv2.imshow("Output", Img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("INFO-", f"{min_val:.3f}", end=" ")

    # 过滤方差过大的匹配结果
    if min_val > Threshold:
        return None
    else:
        return Left_up, Right_down


def Find_in_screen(Img_model_path, Threshold, Flag_show):
    """
    全屏截图 找到与模板匹配的图片区域
    :param Img_model_path:  用来检测的模板图片的路径
    :param Threshold:       匹配的方差阈值 越小越好
    :param Flag_show:       是否输出框选后图片 1为输出
    :return: 返回检测到的区域范围坐标左上和右下
    """
    # 截取屏幕
    Screenshot = pyautogui.screenshot()

    # 将 PIL.Image.Image RGB 对象转换为 OpenCV 的 BGR NumPy 数组
    Img = cv2.cvtColor(np.array(Screenshot), cv2.COLOR_RGB2BGR)

    # 加载图像模板 并读取宽高
    Img_model = cv2.imread(Img_model_path)
    if Img_model is None:
        raise ValueError(f"无法找到文件: {Img_model_path}")
    Img_model_height, Img_model_width = Img_model.shape[0:2]

    # 进行模板匹配 归一化平方差匹配方法 越小越好
    Result = cv2.matchTemplate(Img, Img_model, cv2.TM_SQDIFF_NORMED)

    # 获取匹配结果中的最大值、最小值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Result)

    # 确定识别到的区域
    Left_up = min_loc
    Right_down = (min_loc[0] + Img_model_width, min_loc[1] + Img_model_height)

    print("INFO-", f"{min_val:.3f}", end=" ")
    if Flag_show:
        # 图像上绘制边框
        cv2.rectangle(Img, Left_up, Right_down, (0, 0, 255), 2)

        # 输出标记区域后图案
        cv2.imshow("Output", Img)
        cv2.waitKey(0)

    # 过滤方差过大的匹配结果
    if min_val > Threshold:
        return None
    else:
        return Left_up, Right_down


def Click(Hwnd, Loc, Wait):
    """
    接受一个坐标元组 自动点击
    :param Loc:     坐标元组
    :param Wait:    点击后自动延时的等待时间
    :return: None
    """
    if Hwnd:
        # 计算点击区域在窗口内的绝对坐标
        window_x, window_y, _, _ = win32gui.GetWindowRect(Hwnd)
        ctypes.windll.user32.SetForegroundWindow(Hwnd)
    else:
        window_x, window_y = 0, 0

    # 计算出识别区域长宽 然后点击区域中随机坐标
    Width = Loc[1][0] - Loc[0][0]
    Height = Loc[1][1] - Loc[0][1]

    loc_x = window_x + Loc[0][0] + Width / 4 + random.randint(0, Width) / 2
    loc_y = window_y + Loc[0][1] + Height / 4 + random.randint(0, Height) / 2

    # 点击窗口内的指定区域
    pyautogui.click(x=loc_x, y=loc_y, button="left")
    time.sleep(Wait)


def Find_Click_windows(Hwnd, Model_path, Threshold, message_F, message_C):
    while not config.stop_thread:
        try:
            Range = Find_in_windows(Hwnd, Model_path, Threshold, 0)
            Click(Hwnd, Range, 1)
            # pyautogui.moveTo(10, 10)
            print(message_F)
            return 1
        except:
            print(message_C)
            # config.stop_thread = True
            return 0


def Find_Click_screen(Model_path, Threshold, message_F, message_C):
    while not config.stop_thread:
        try:
            Range = Find_in_screen(Model_path, Threshold, 0)
            Click(None, Range, 1)
            # pyautogui.moveTo(10, 10)
            print(message_F)
            return 1
        except:
            print(message_C)
            # config.stop_thread = True
            return 0


def read_config(FILE_PATH):
    """
    读取配置文件
    """
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return {}


def write_config(FILE_PATH, data):
    """
    将配置写入 JSON 文件
    """
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def check_lasttime(Account, Times_name):
    """
    检测上次运行的时间
    """
    config = read_config("./config/Last_times.json")
    Times_need_str = config[Account].get(Times_name, None)
    Times_need = datetime.fromisoformat(Times_need_str) if Times_need_str else None
    if Times_need is not None:
        print(f"TIME- ----- {Times_need.strftime('%Y-%m-%d %H:%M:%S')}")
        return Times_need
    else:
        print("TIME- ----- 没有记录上次时间 已重置初始化值")
        Initial_time = datetime(2000, 1, 1, 0, 0)
        config[Account][Times_name] = Initial_time.isoformat()
        write_config("./config/Last_times.json", config)
        return Initial_time


def Itface_Quit(Hwnd):
    """
    检测是否有退出界面 有则esc解除
    :param Hwnd:    窗口句柄
    :return: None
    """
    time.sleep(3)
    # 注：此处退出界面条件可以极为苛刻 一般识别取值为0.006
    Range = Find_in_screen("./pic/Main/Tuichuyouxi.png", 0.01, 0)
    if Range:
        print("检测到退出界面")
        Range = Find_in_screen("./pic/Main/Quxiaotuichu.png", 0.05, 0)
        Click(None, Range, 1)
        print("取消退出")
    else:
        print("未检测到退出界面")


def Itface_Host(Hwnd):
    """
    检测是否处在主界面
    :param Hwnd:    窗口句柄
    :return: None
    """
    Wait = 0
    while True:
        # Itface_Quit(Hwnd)
        time.sleep(0.5)
        # 检测到庭院 退出循环
        ctypes.windll.user32.SetForegroundWindow(Hwnd)
        if Find_in_windows(Hwnd, "./pic/Main/Zhujiemian.png", 0.05, 0):
            Itface = "Host"
            print("检测到进入庭院")
            return 1
            break
        Wait += 2
        time.sleep(1)

        if Wait >= 10:
            # 按esc尝试回到主界面
            pydirectinput.press("esc")
            print("未检测到进入庭院 尝试esc")
            Itface_Quit(Hwnd)

            # 检测弹窗
            Range = Find_in_windows(Hwnd, "./pic/Main/Cha.png", 0.06, 0)
            if Range:
                # 点击弹窗插
                Click(Hwnd, Range, 1)
                print("关闭弹窗")
            else:
                print("未检测到弹窗")
        else:
            print("未检测到进入庭院")

        # 30s未检测到 超时退出
        if Wait >= 30:
            Wait = 0
            print("EROR- ***** 进入庭院 超时退出 ********************************")
            return 0
            exit()


def Itface_scroll(Hwnd):
    """
    位于庭院时 检测并确保卷轴打开
    @param Hwnd:    窗口句柄
    @return:        1正常0异常
    """
    # 检测是否位于庭院主界面
    Itface_Host(Hwnd)

    # 检测底部卷轴是否展开
    Range = Find_in_windows(Hwnd, "./pic/Thr/Shishenlu.png", 0.05, 0)
    if not Range:
        print("检测到卷轴尚未打开 点击打开卷轴")
        # 坐标法点击展开卷轴
        Range = ((1780, 970), (1910, 1120))
        Click(Hwnd, Range, 2)

        Range = Find_in_windows(Hwnd, "./pic/Thr/Shishenlu.png", 0.05, 0)
        if Range:
            print("检测到卷轴已经打开")
        else:
            print("打开卷轴失败")
            return 0
    else:
        print("检测到卷轴已经打开")
        return 1


def Itface_guild(Hwnd):
    """
    位于庭院时 进入阴阳寮界面
    @param Hwnd:    窗口句柄
    @return:        1正常0异常
    """
    # 确保卷轴打开
    Itface_scroll(Hwnd)

    # 进入阴阳寮
    Range = Find_in_windows(Hwnd, "./pic/Sis/Yinyangliao.png", 0.05, 0)
    if Range:
        Click(Hwnd, Range, 1)
        print("进入阴阳寮")
        time.sleep(1)
        return 1
    else:
        print("进入阴阳寮失败")
        return 0


def Itface_daily(Hwnd):
    """
    循环检测多种外显的日常入口
    """
    for i in range(1):
        if Find_Click_windows(Hwnd, "./pic/Main/Fengmorukou.png", 0.05, "进入逢魔入口", "未检测到逢魔入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Doujirukou.png", 0.05, "进入斗技入口", "未检测到斗技入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Yinjiezhimenrukou.png", 0.05, "进入阴界之门入口", "未检测到阴界之门入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Daoguanrukou.png", 0.05, "进入道馆入口", "未检测到道馆入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Baiguiyirukou.png", 0.05, "进入百鬼弈入口", "未检测到百鬼弈入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Xiajiananyurukou.png", 0.05, "进入狭间暗域入口", "未检测到狭间暗域入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Qilinrukou.png", 0.05, "进入麒麟入口", "未检测到麒麟入口"):
            break
        if Find_Click_windows(Hwnd, "./pic/Main/Yanhuirukou.png", 0.05, "进入宴会入口", "未检测到宴会入口"):
            break


def Itface_explore(Hwnd):
    """
    位于庭院时 进入探索界面
    param Hwnd:    窗口句柄
    """
    # 检测是否位于庭院主界面
    Itface_Host(Hwnd)
    Find = Find_Click_windows(Hwnd, "./pic/Main/Feng.png", 0.05, "进入悬赏封印界面", "未进入悬赏封印界面")
    if not Find:
        Find_Click_windows(Hwnd, "./pic/Main/Feng.png", 0.05, "进入悬赏封印界面", "未进入悬赏封印界面")

    Find = Find_Click_windows(Hwnd, "./pic/Main/Xuanshangxing.png", 0.05, "点击悬赏星", "未检测到悬赏星")
    Find = Find_Click_windows(Hwnd, "./pic/Main/Xuanshangqianwang.png", 0.05, "进入探索地图界面", "未进入探索地图界面")

    time.sleep(1)
    Esc_print()
    time.sleep(1)

    if Find_in_windows(Hwnd, "./pic/Digui/Diguitubiao.png", 0.05, 0):
        print("检测到地鬼入口 已进入探索界面")
    else:
        print("未检测到地鬼入口 似乎未进入探索界面")
        Esc_print()
