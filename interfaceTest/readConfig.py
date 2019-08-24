import os
import codecs
import configparser
#获取配置文件路径
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig:
    def __init__(self):
        #创建对象
        self.cf = configparser.ConfigParser()
        #读取配置
        self.cf.read(configPath)

    #获取对应配置信息
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value


    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


