# -*-coding:utf-8-*-
from lib.UiautomatorLib import *


def get_random_num(min=0, max=20):
    """获取随机数"""
    random_num = random.randint(min, max)
    log.logger.debug('random_num：%s' % random_num)
    return random_num


if __name__ == '__main__':
    print(os.path.split(os.path.abspath(".."))[1])
