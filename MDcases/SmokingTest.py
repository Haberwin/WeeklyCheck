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
from . import screenshot


class TestWeekly(unittest.TestCase):
    """测试屏幕截图"""

    @screenshot
    def test01(self):
        """拨打电话"""
        i = 0
        for i in range(10):
            print(i)
        self.assertEqual(i, 9)

    @screenshot
    def test02(self):
        """测试截图"""
        j = 0
        for j in range(10,20):
            print(j)
        self.assertEqual(j, 11)


if __name__ == '__main__':
    pass
