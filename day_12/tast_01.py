import requests
import unittest
import HTMLTestRunnerNew
import time
from day_12.http_requests import HttpRequests

# key ：863a9a944d6a397a16f74c4202127b70
#编写测试类
class TestHttpRequests(unittest.TestCase):
    def setUp(self):  # 做初始化工作
        self.url = "http://v.juhe.cn/laohuangli/d"
        self.param = {'date': '2018-06-23', 'key': '863a9a944d6a397a16f74c4202127b71'}

    def test_get_request(self):
        t = HttpRequests(self.url, self.param)
        response = t.get_post_request('get')
        self.assertEqual('successed', response['reason']) # 把期望值放前面
        # 期望值和实际值进行对比
        # 每一条用例至少有一个断言

    def tearDown(self):
        pass

# 存放用例的suite 测试套件
suite = unittest.TestSuite()
suite.addTest(TestHttpRequests('test_get_request'))

# 引入时间（防止报告被覆盖）
now =time.strftime('%Y-%m-%d_%H_%M_%S') #获取当前时间
file_path = 'test'+now+'.html'
# 执行用例
with open(file_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='单元测试用例报告',description='测试用例的执行',tester='natu')
    runner.run(suite)