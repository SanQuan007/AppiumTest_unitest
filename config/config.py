# -*- coding: utf-8 -*-


COMMON_CFG = {
    "URL": "http://127.0.0.1:4723/wd/hub",  # appium默认设置URl，需要注意端口与本机启动端口一致
    "LOG_PATH": "E:/workspaces/AppiumTest/logs/",  # log日志、错误截图、测试报告存放地址
    "PROJECT_PATH": "E:/workspaces/AppiumTest/suite/",  # 项目文件所在的目录，可在suite目录下存放多个项目文件
    "CURRENT_PROJECT_NAME": "douyin",  # 需要批量执行的项目名，与suite目录下该项目的目录名称相同；若设置项目名，则批跑脚本只会执行该项目下的测试文件，若设置为空则执行所有项目
    # "CURRENT_PROJECT_NAME": None,
    "LOG_LEVEL": "debug"  # 日志输出级别
}
