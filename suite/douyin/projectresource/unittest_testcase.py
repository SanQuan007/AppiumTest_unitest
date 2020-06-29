#-*-coding:utf-8-*-
import unittest
from suite.douyin.projectresource.commonprojectresource import *

class OTestCase(unittest.TestCase):

    def setUp(self):
        self.com = CommonProjectresource()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()