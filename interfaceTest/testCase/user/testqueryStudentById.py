# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import unittest
import requests
import paramunittest
import readConfig as readConfig
from common import common
from common import configHttp
from common.Log import Logg
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
queryStudentById_xls = common.get_xls("userCase.xlsx", "queryStudentById")
log=Logg();

@paramunittest.parametrized(*queryStudentById_xls)
# 根据学员ID查询学员  http://api-shuangshi.tengyue360.com/backend/student/student/queryStudentById
class QueryStudentById(unittest.TestCase):
    def setParameters(self, case_name, method, url, parameter, resultType, errno, error, cityName):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.parameter = str(parameter)
        self.resultType = str(resultType)
        self.errno = str(errno)
        self.error = str(error)
        self.cityName = str(cityName)

    def description(self):
        self.case_name

    def setUp(self):
        # 初始化
        # 初始化
        logger = log.get_logger();
        logger.info("课程列表")

    # 获取url地址
    def test_QueryStudentById(self):
        '''根据学员id查询学员信息接口'''
        localConfigHttp.set_url(self.url)
        # 获取commontoken信息
        token_v = common.get_visitor_token();
        header = {"Content-Type": 'application/json', "authorization": token_v}
        localConfigHttp.set_headers(header)
        # set param
        localConfigHttp.set_data(self.parameter)
        # 请求对应封装接口
        self.respon = localConfigHttp.postWithJson()
        # 调用checkResult方法
        self.checkResult()

    def tearDown(self):
        pass

    # 较验json格式返回值
    def checkResult(self):
        # 获取json格式值
        self.info = self.respon.json()
        common.show_return_msg(self.respon)
        self.info = self.respon.json()
        # 判断状态是否是200
        if self.respon.status_code == 200 and self.resultType == 0:
            print(self.info['error'])
            # 断言返回值errno, cityname,error是否成功
            self.assertEqual(self.info['errno'], int(self.errno))
            self.assertEqual(self.info['data']['cityName'], self.cityName)
            self.assertEqual(self.info['error'], "操作成功")
