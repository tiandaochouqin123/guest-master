# -*- coding: cp936 -*-
#coding = utf-8

import unittest, time, re
import HTMLTestRunner
import xlrd
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')


def creatsuite():

    #1---找到所有的test*py文件
    testunit = unittest.TestSuite()
    #定义测试文件查找目录
    test_dir = 'C:\\Users\\刘巍\\Desktop\\guest-master\\tests'

    #定义discover方法的参数
    discover= unittest.defaultTestLoader.discover(

            test_dir,
            pattern = '*test.py',
            top_level_dir = None

            )

        
    return testunit


#3---测试报告
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。
filename = "C:\\Users\\刘巍\\Desktop\\guest-master\\report"+now+'result.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='iwebshop_test_report',
    description=u'test_case_description')



if __name__ == '__main__':
    #调用creatsuite方法，返回需要添加的test*.py文件组成的测试套件
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
