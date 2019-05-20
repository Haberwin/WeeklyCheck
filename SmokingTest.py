# -*-coding:utf-8-*-
import traceback
import unittest
import HTMLTestReportCN


class TestWeekly(unittest.TestCase):
    """测试屏幕截图"""
    def test01(self):
        i = 0
        for i in range(10):
            print(i)
        self.assertEqual(i, 9)

    def test02(self):
        """测试2"""
        j=0
        for j in range(10):
            print(j)
        try:
            self.assertEquals(j, 11)
        except:
            traceback.print_exc()

            print("screenshot:../screenshot/2019-05-24-10-23-33.png")
            raise




if __name__ == '__main__':
    filepath = './result/htmlreport.html'
    with open(filepath, 'wb') as ftp:
        suite = unittest.TestSuite(unittest.makeSuite(TestWeekly))
        # suite.addTest(TestWeekly('test01'))
        # suite.addTest(TestWeekly('test02'))
        runner = HTMLTestReportCN.HTMLTestRunner(stream=ftp, title='Weekly test Result', tester="MD-VAL")
        runner.run(suite)
        unittest.main()
