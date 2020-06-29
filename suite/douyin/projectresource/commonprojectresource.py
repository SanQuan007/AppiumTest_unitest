#-*-coding:utf-8-*-
from lib.UiautomatorLib import *
from suite.douyin.projectlib.libprojectresource import *


class CommonProjectresource(object):
    """通用模块"""

    # 当前运行的脚本路径
    config.COMMOM_CFG["CURRENT_PROJECT_NAME"] = 'douyin'
    log.logger.info('CURRENT_PROJECT_NAME：%s'%config.COMMOM_CFG["CURRENT_PROJECT_NAME"])

    def __init__(self):
        self.auto = UiautoLib()

    def LogIn(self, dict):
        """登录用户"""
        username = dict.get("username")
        password = dict.get("password")
        log.logger.info("input values:" + str(dict))
        dict.clear()
        #点击“好的”
        self.auto.Click("首页_个人信息保护指引_BUTTON_好的")
        # # 点击“始终允许”
        self.auto.ExistClick("系统_获取手机号及通话状态_BUTTON_始终允许")
        # #点击“始终允许”
        self.auto.ExistClick("系统_获取设备的定位信息_BUTTON_始终允许")
        # 点击“红包×号”
        self.auto.Click("首页_红包_BUTTON_CLOSE")
        self.auto.SwipeUp()
        # 点击“我的”
        self.auto.Click("首页_状态栏_BUTTON_我")
        time.sleep(10)
        # 点击“其他手机号登陆”
        self.auto.Click("我_登录页面_BUTTON_其他手机号登录")
        # 点击“其他密码登录”
        self.auto.Click("我_登录页面_BUTTON_密码登录")
        # 点击“登录账号”
        self.auto.SendText("我_登录页面_EDITTEXT_账号", username)
        # 输入“登录密码”
        self.auto.SendText("我_登录页面_EDITTEXT_密码", password)
        # 点击“同意协议书”
        self.auto.Click("我_登录页面_RADIOBOX_同意协议书")
        # 点击“登录”
        self.auto.Click("我_登录页面_BUTTON_登录")
        # 点击“我的”
        self.auto.Click("首页_状态栏_BUTTON_我")
        self.auto.ExistClick("其他_隐私政策_BUTTON_返回")
        self.auto.Click("首页_状态栏_BUTTON_我")
        time.sleep(5)
        #获取登录后的用户名
        username = self.auto.GetText("我_登录页面_TEXT_用户名")
        #获取登录后的抖音号
        douyin_number = self.auto.GetText("我_登录页面_TEXT_抖音号")
        # 点击“首页”
        self.auto.Click("首页_状态栏_BUTTON_首页")

        dict["username"] = username
        dict["douyin_number"] = douyin_number
        return dict

    def SwipeUpForLoop(self, dict):
        """向下滑动指定次数"""
        swipe_num = dict.get("swipe_num")
        log.logger.info("input values:" + str(dict))
        flag = True
        i = 1
        while flag:
            self.auto.SwipeUp()
            num = get_random_num()
            time.sleep(num)
            i += 1
            if swipe_num and i >= swipe_num:
                flag = False

if __name__ == '__main__':
    print(os.path.split(os.path.abspath(".."))[1])