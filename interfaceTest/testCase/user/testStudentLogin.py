# -*- coding:utf-8 -*-
import unittest
import paramunittest




#调用方法
#读取配置信息
from interfaceTest import readConfig
from interfaceTest.common import common
from interfaceTest.common.Log import Logg
import configHttp

localReadConfig = readConfig.ReadConfig()
#调用get post封装的请求方法
localConfigHttp = configHttp.ConfigHttp()
#调用读取excel方法
studentLogin_xls = common.get_xls("userCase.xlsx", "studentLogin")
#调用log中的方法
log=Logg();
#参数化
@paramunittest.parametrized(*studentLogin_xls)
class StudentLogin(unittest.TestCase):
    global log, logger, resultPath
    def setParameters(self, case_name, method, url, parameter, resultType, errno, error):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.parameter = str(parameter)
        self.resultType = str(resultType)
        self.errno = str(errno)
        self.error = str(error)

    def test_login(self):
        '''学生端登陆'''
        localConfigHttp.set_url(self.url)
        header = {"Content-Type": 'application/json'}
        localConfigHttp.set_headers(header)
        localConfigHttp.set_data(self.parameter)
        # 请求对应封装接口
        self.respon = localConfigHttp.postWithJson()
        # 调用checkResult方法
        self.checkResult();

    def setUp(self):
        # 初始化
        logger = log.get_logger();
        logger.info("登陆")

    # 较验json格式返回值
    def checkResult(self):
        # 获取json格式值
        self.info = self.respon.json()
        common.show_return_msg(self.respon)
        # 判断状态是否是200
        if self.resultType == '0' and self.respon.status_code == 200:
            self.assertEqual(self.info['errno'], int(self.errno))
            self.assertEqual(self.info['error'], "操作成功");
        elif self.resultType == '1' and self.respon.status_code == 200:
            self.assertEqual(self.info['errno'], int(self.errno))
            self.assertEqual(self.info['error'], self.error);
        elif self.resultType == '2' and self.respon.status_code == 200:
            self.assertEqual(self.info['errno'], int(self.errno))
            self.assertEqual(self.info['error'], self.error);

if __name__ == '__main__':
    unittest.main()
