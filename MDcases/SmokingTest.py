# -*-coding:utf-8-*-
import functools
import time
import sys
import traceback
import unittest
import HTMLTestReportCN
import subprocess
import os
import functools
# from . import screenshotX


class TestWeekly(unittest.TestCase):
    """测试屏幕截图"""

    def screenshot(self) -> None:
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        sys.stdout.write("screenshot:../screenshot/{timestamp}.png".format(timestamp=timestamp))
        path = os.getcwd() + "/screenshot"
        process = subprocess.Popen("adb shell screencap -p /data/local/tmp/screen.png", shell=True)
        process.wait()
        subprocess.run(
            "adb pull /data/local/tmp/screen.png {path}/{timestamp}.png".format(path=path, timestamp=timestamp),
            shell=True)
        subprocess.run("adb shell 'rm /data/local/tmp/screen.png'", shell=True)

    def test01(self):
        """拨打电话"""
        i = 0
        for i in range(10):
            print(i)
        self.screenshot()
        self.assertEqual(i, 9)


    def test02(self):
        """测试截图"""
        j = 0
        for j in range(10,20):
            print(j)
        self.screenshot()
        self.assertEqual(j, 11)


