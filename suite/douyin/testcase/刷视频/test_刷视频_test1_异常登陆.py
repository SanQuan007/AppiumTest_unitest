#-*-coding:utf-8-*-
from suite.douyin.projectresource.unittest_testcase import * 

class TestCase(OTestCase):
	def testRun(self):
		#------------------------------步骤1|com.LogIn|登陆用户---------------------------------
		try:
			log.logger.info('\n' + 20 * '* ' + '步骤1|com.LogIn|登陆用户' + 20 * ' *')
			dict = {
				'username': '187XXXXX',
				'password': '密码XXXX',
			}
			self.dict_step1 = self.com.LogIn(dict)
			self.assertEqual(self.dict_step1.get('用户名'), 'username')
			self.assertEqual(self.dict_step1.get('抖音号：XXX'), 'douyin_number')
			status = 'Success'
		except Exception as e:
			status = 'Fail'
			log.logger.error(e)
			raise e
		finally:
			log.logger.info('\n' + 20 * '* ' + '步骤1|com.LogIn|登陆用户 ' + status + 20 * ' *')
		#------------------------------步骤2|com.SwipeUpForLoop|滑动屏幕，切换视频---------------------------------
		try:
			log.logger.info('\n' + 20 * '* ' + '步骤2|com.SwipeUpForLoop|滑动屏幕，切换视频' + 20 * ' *')
			dict = {
				'swipe_num': 10,
			}
			self.dict_step2 = self.com.SwipeUpForLoop(dict)
			self.assertEqual(self.dict_step2.get('self.dict_step1.username'), 'username')
			status = 'Success'
		except Exception as e:
			status = 'Fail'
			log.logger.error(e)
			raise e
		finally:
			log.logger.info('\n' + 20 * '* ' + '步骤2|com.SwipeUpForLoop|滑动屏幕，切换视频 ' + status + 20 * ' *')
if __name__ == '__main__':
	unittest.main()