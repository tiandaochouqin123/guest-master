#-*- coding:utf-8 -*-

import unittest, time, re
import HTMLTestRunner
import xlrd
import sys
import time

def all_case():

	case_dir = "C:\\Users\\刘巍\\Desktop\\guest-master\\tests"

	testcase = unittest.TestSuite()

	discover= unittest.defaultTestLoader.discover(

            case_dir,
            pattern = "*_test.py",
            top_level_dir = None

            )

	testcase.addTests(discover)
	

	#print (testcase)
            
	return testcase


if __name__== "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    runner = unittest.TextTestRunner()
    #filename = "C:\\Users\\刘巍\\Desktop\\guest-master\\result.html"
    filename = "C:\\Users\\刘巍\\Desktop\\guest-master" + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,
                                        title='Guest Manage System Interface Test Report',
                                         description='Implementation Example with:')
    runner.run(all_case())
    fp.close()
'''	alltestnames = all_case()
	runner.run(alltestnames)
	fp.close()'''
