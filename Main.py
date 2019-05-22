# -*-coding:utf-8-*-
import subprocess
import unittest

from uiautomator import Device,Adb

import HTMLTestReportCN
from MDcases import *

def init_devices():
    subprocess.run("adb push ./Apks/app-uiautomator.apk /data/local/tmp/",shell=True)
    subprocess.run("adb push ./Apks/app-uiautomator-test.apk /data/local/tmp/", shell=True)
    subprocess.run("adb shell pm install -r -t /data/local/tmp/app-uiautomator.apk", shell=True)
    subprocess.run("adb shell pm install -r -t /data/local/tmp/app-uiautomator.apk", shell=True)

if __name__ =='__main__':
    # init_devices()
    d=Device("18011B1AC8")
    d.press.home()

    filepath = './result/htmlreport.html'
    with open(filepath, 'wb') as ftp:
        suite = unittest.TestSuite(unittest.makeSuite(SmokingTest.TestWeekly))
        # suite.addTest(TestWeekly('test01'))
        # suite = unittest.TestSuite()
        # suite.addTest(TestWeekly('test02'))
        runner = HTMLTestReportCN.HTMLTestRunner(stream=ftp, title='Weekly test Result', tester="MD-VAL")
        runner.run(suite)
        unittest.main()
