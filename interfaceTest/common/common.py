import requests
#获取config里面的信息

import os
from xlrd import open_workbook

from interfaceTest.common import configHttp
from interfaceTest.common.Log import Logg

log=Logg()#调用初始化
import json

#导入方法读取baseurl
localReadConfig = readConfig.ReadConfig()
#获取文件的路径
proDir = readConfig.proDir
#这里调用了
localConfigHttp = configHttp.ConfigHttp()

#获取学生端登陆token 公共方法
def get_visitor_token():
    send_param = {"phone": 14050000000, "password": "e10adc3949ba59abbe56e057f20f883e", "messageCode": "0",
        "loginType": "1", "timestamp": "0"}
    urllist = localReadConfig.get_http("BASEURL")
    #http://api-shuangshi.tengyue360.com
    headers = {"Content-Type": 'application/json'}
    res = requests.post("http://"+urllist + "/backend/student/unauth/login",data=json.dumps(send_param), headers=headers)
    info = res.json()
    #header中获取token
    token=res.headers['authorization']
    #logger=log.get_logger()
    #logger.debug("Create token:%s" % (token))
    return token

#报告返回接口信息信息公共方法
def show_return_msg(response):
    # 返回response返回信息
    url = response.url
    # 返回json返回值
    msg = response.text
    print("\n请求地址：" + url)
    # 可以显示中文
    print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # 获取xls文件的路径
    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
    #D:\interfaceTest\testFile\case\userCase.xlsx
    # 打开文件
    file = open_workbook(xlsPath)
    # 按照名称获取工作列表
    sheet = file.sheet_by_name(sheet_name)
    # 获取页的一行
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

if __name__ == "__main__":
    get_visitor_token();
