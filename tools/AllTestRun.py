# -*-coding:utf-8-*-
import unittest
from config.config import COMMOM_CFG
from tools.HTMLTestRunner import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner
import datetime
import os


def allTest():
    suite_dir = COMMOM_CFG.get("PROJECT_PATH")
    projects = list(set(os.listdir(suite_dir)) - set([name for name in os.listdir(suite_dir) if name.startswith("_")]))
    # 执行匹配条件的测试用例
    suite = unittest.TestSuite()
    if COMMOM_CFG["CURRENT_PROJECT_NAME"]:
        project_name = os.path.join(suite_dir, COMMOM_CFG["CURRENT_PROJECT_NAME"])
        discover = unittest.defaultTestLoader.discover(project_name, pattern='test*.py')
        suite.addTest(discover)
        return suite
    else:
        for project in projects:
            project_name = os.path.join(suite_dir, project)
            discover = unittest.defaultTestLoader.discover(project_name, pattern='test*.py')
            suite.addTest(discover)
        return suite


if __name__ == '__main__':
    report_dir = COMMOM_CFG.get("LOG_PATH")
    # current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    # report_name = report_dir + current_time + '_report.html'
    report_name = report_dir + 'report.html'
    from lib.SysLib import Logger

    logger = Logger().logger
    runner = HTMLTestRunner(stream=open(report_name, "wb"), verbosity=2, logger=logger, retry=0, save_last_try=True)
    runner.run(allTest())
