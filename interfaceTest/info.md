接口自动化1.0版本
#目录说明
 common：存放一些公共的方法（token,读取excel公共方法，封装请求方法等，获取coolie等）
 result：执行过程中生成的文件夹，里面存放每次测试的结果
 testCase：用于存放具体的测试case
 testFile：存放测试过程中用到的文件，包括上传的文件，测试用例
 caselist：txt文件，配置每次执行的case名称
 config：配置一些常量，例如数据库的相关信息，接口的相关信息参数等
 readConfig： 用于读取config配置文件中的内容
 runAll：用于执行case
 #版本支持python 3以上（本人使用3.7）


 #所学习知识点
 1.python基础必须会
 2.requests api必须会
 3.python学习笔记之读取配置文件必须会（configparser）备注：http://zixuephp.net/article-431.html
 4.logging模块使用教程（https://www.jianshu.com/p/feb86c06c4f4）
 5.python excel读取
 6.unittest参数化（paramunittest）：https://blog.csdn.net/qq_39208536/article/details/80738508
 7.HTMlTestRunner报告如何加载修改


 接口自动测试流程->抓包/postman使用->requests->logging->配置文件读取->xml->excel等等-》到搭建-〉项目持续集成妥妥的

 ###############################################################