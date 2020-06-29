#coding:utf-8
from appium import webdriver
from lib.SysLib import *
import time

class UiautoLib(object):
    def __init__(self):
        self.driver = webdriver.Remote(config.COMMOM_CFG["URL"], get_appium_capability())
        self.find_element_number = 5
        self.sleep_time = 2

    def Click(self, locator=None, driver_element=None):
        """根据坐标点击元素"""
        if not driver_element:
            driver_element = self.find_element(locator)
        location = driver_element.location
        size = driver_element.size
        location_x = location["x"]
        location_y = location["y"]
        location_w = location["x"] + size["width"]
        location_h = location["y"] + size["width"]
        log.logger.debug('location_x：%s，location_y：%s，location_w：%s，location_h：%s' % \
                        (location_x, location_y, location_w, location_h))
        self.driver.tap([(location_x, location_y), (location_w, location_h)], 100)

    def ExistClick(self, locator):
        """元素如果不存在页面上则不点击"""
        driver_element = self.find_element_is_exist(locator)
        if not driver_element:
            return False
        else:
            self.Click(driver_element=driver_element)

    def GetText(self, locator):
        """获取text属性"""
        driver_element = self.find_element(locator)
        text = driver_element.text
        log.logger.debug('text：%s' % text)
        return text

    def SendText(self, locator, text):
        """输入text信息
        若出现使用该函数无法输入的情况，
        可使用click+input text组合输入的方式
        """
        driver_element = self.find_element(locator)
        driver_element.clear()
        driver_element.send_keys(text)

    def SwipeUp(self, num =1):
        """向上滑动屏幕"""
        self.swipe_diff_direection("up", num)

    def SwipeDown(self, num =1):
        """向下滑动屏幕"""
        self.swipe_diff_direection("down", num)

    def SwipeLeft(self, num =1):
        """向左滑动屏幕"""
        self.swipe_diff_direection("left", num)

    def SwipeRight(self, num =1):
        """向右滑动屏幕"""
        self.swipe_diff_direection("right", num)

    def swipe_diff_direection(self, direction, n=1 ,t=500):
        '''向不同的方向滑动屏幕'''
        window_size = self.driver.get_window_size()
        xc = window_size['width'] * 0.5  # x 坐标
        x1 = window_size['width'] * 0.75  # x 坐标
        x2 = window_size['width'] * 0.25  # x 坐标
        yc = window_size['height'] * 0.5
        y1 = window_size['height'] * 0.75  # 起始 y 坐标
        y2 = window_size['height'] * 0.25  # 终点 y 坐标
        if direction.lower() == "up":
            log.logger.debug('direction：%s，x1：%s，y1：%s，x2：%s，y2：%s，'\
                             %(direction, xc ,y1 ,xc ,y2))
            self.driver.swipe(xc, y1, xc, y2, t)
        if direction.lower() == "down":
            for i in range(n):
                log.logger.debug('direction：%s，x1：%s，y1：%s，x2：%s，y2：%s，' \
                                 % (direction, xc, y2, xc, y1))
                self.driver.swipe(xc, y2, xc, y1, t)
        if direction.lower() == "left":
            for i in range(n):
                log.logger.debug('direction：%s，x1：%s，y1：%s，x2：%s，y2：%s，' \
                                 % (direction, x2, yc, x1, yc))
                self.driver.swipe(x2, yc, x1, yc, t)
        if direction.lower() == "right":
            for i in range(n):
                log.logger.debug('direction：%s，x1：%s，y1：%s，x2：%s，y2：%s，' \
                                 % (direction, x1, yc, x2, yc))
                self.driver.swipe(x1, yc, x2, yc, t)

    def SwipeToElement(self, locator):
        """滚动到指定的元素"""
        driver_element = self.find_element(locator)
        self.driver.execute_script("mobile: scroll", {"direction": "down", "element": driver_element})

    def Shake(self):
        """摇一摇手机"""
        self.driver.shake()

    def Reset(self):
        """重置手机(类似于清除缓存)"""
        self.driver.reset()

    def HideKeyboard(self):
        self.driver.hide_keyboard()

    def find_element(self, locator_key):
        locator_value = get_locator_value(locator_key)
        class_name = locator_value[0:2].lower()
        locator = locator_value[3:]
        driver_element = None
        for i in range(self.find_element_number):
            try:
                if class_name == "id":
                    driver_element = self.driver.find_element_by_id(locator)
                if class_name == "na":
                    driver_element = self.driver.find_element_by_name(locator)
                if class_name == "xp":
                    driver_element = self.driver.find_element_by_xpath(locator)
                return driver_element
            except Exception as e:
                time.sleep(self.sleep_time)
        error_message = "页面未找到该元素：%s" % (locator_key)
        log.logger.error(error_message)
        raise Exception(error_message)

    def find_element_is_exist(self, locator_key):
        locator_value = get_locator_value(locator_key)
        class_name = locator_value[0:2].lower()
        locator = locator_value[3:]
        driver_element = None
        for i in range(self.find_element_number):
            try:
                if class_name == "id":
                    driver_element = self.driver.find_element_by_id(locator)
                if class_name == "na":
                    driver_element = self.driver.find_element_by_name(locator)
                if class_name == "xp":
                    driver_element = self.driver.find_element_by_xpath(locator)
                return driver_element
            except Exception as e:
                time.sleep(self.sleep_time)
        error_message = "页面未找到该元素：%s" % (locator_key)
        log.logger.info(error_message)
        return False

    def get_page_source(self):
        """获取页面源码"""
        self.driver.page_source()
        print(self.driver.page_source())

if __name__ == '__main__':
    error_message = "页面未找到该元素：%s\n屏幕截图地址：%s" % (1, 2)
    print(error_message)