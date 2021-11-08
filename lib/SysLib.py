# -*- coding: utf-8 -*-
import random
import os
import datetime
import sys
import importlib
from varible.locator import COMMON_LOCATOR
from config import config
from lib.LogLib import Logger

# 定义日志
log = Logger()

# 当前运行的脚本路径
CURRENT_FILE_NAME = sys.argv[0]


def get_locator_value(locator_key):
    """根据loctor.py的key值获取value"""
    project_name = config.COMMON_CFG["CURRENT_PROJECT_NAME"]
    project_varible_path = 'suite.%s.projectvaible.locator' % project_name
    log.logger.debug('project_varible_path：%s' % project_varible_path)
    import_project_varible = importlib.import_module(project_varible_path)
    PROJECT_LOCATOR = import_project_varible.PROJECT_LOCATOR
    log.logger.debug('locator_name：%s' % locator_key)
    page_name = locator_key.split("_")[0]
    try:
        locator_value = PROJECT_LOCATOR.get(page_name).get(locator_key)
    except Exception as e:
        locator_value = COMMON_LOCATOR.get(page_name).get(locator_key)
    if not locator_value:
        locator_value = COMMON_LOCATOR.get(page_name).get(locator_key)
    log.logger.debug('locator_value：%s' % locator_value)
    return locator_value


def send_cmd_screenshots():
    """获取当前界面的截图以及uix文件"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    file_name = config.COMMON_CFG["LOG_PATH"] + "UIautomatorPng/" + current_time + "/ScreenPng"
    log.logger.debug('log_screen_file_name：%s' % file_name)
    mkdir(file_name)
    cmd_1 = "adb shell /system/bin/uiautomator dump /sdcard/app.uix"
    cmd_2 = "adb pull /sdcard/app.uix " + file_name + "/app.uix"
    cmd_3 = "adb shell /system/bin/screencap -p /sdcard/app.png"
    cmd_4 = "adb pull /sdcard/app.png " + file_name + "/app.png"
    for cmd in [cmd_1, cmd_2, cmd_3, cmd_4]:
        send_link_by_cmd(cmd)
    return file_name


def get_appium_capability():
    """获取Appium 服务器初始化参数"""
    project_name = config.COMMON_CFG["CURRENT_PROJECT_NAME"]
    project_varible_path = 'suite.%s.projectconfig.config' % project_name
    log.logger.debug('project_varible_path：%s' % project_varible_path)
    import_project_locator = importlib.import_module(project_varible_path)
    APPIUM_CAPABILITY = import_project_locator.APPIUM_CAPABILITY
    log.logger.info('APPIUM_CAPABILITY：%s' % APPIUM_CAPABILITY)
    return APPIUM_CAPABILITY


def send_link_by_cmd(cmd):
    """传入命令，在windows中执行"""
    log.logger.debug('cmd：%s' % cmd)
    ret = os.system(cmd)
    return ret


def mkdir(path):
    """创建目录"""
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        log.logger.debug('mkdir_path：%s' % path)
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':
    # send_screenshots_order()
    pass
