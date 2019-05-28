# -*-coding:utf-8-*-
import platform
import subprocess
import unittest
import configparser
from uiautomator import Device, Adb
import HTMLTestReportCN


from MDcases import *


def mount_smb(sudo_psw, server_dir, target_dir, username, password) -> bool:
    p1 = subprocess.Popen(
        r"echo {sudo_psw}|sudo -S mount -t cifs {server_dir} {target_dir} -o username={username},password={password}".format(
            sudo_psw=sudo_psw, server_dir=server_dir, target_dir=target_dir, username=username, password=password),
        shell=True,
        stderr=subprocess.PIPE, encoding='utf-8')
    err = p1.stderr.readline()
    return (err.endswith(': ') or err.__contains__('mount error(16): Device or resource busy'))


def init_devices():
    subprocess.run("adb push ./Apks/app-uiautomator.apk /data/local/tmp/", shell=True)
    subprocess.run("adb push ./Apks/app-uiautomator-test.apk /data/local/tmp/", shell=True)
    subprocess.run("adb shell pm install -r -t /data/local/tmp/app-uiautomator.apk", shell=True)
    subprocess.run("adb shell pm install -r -t /data/local/tmp/app-uiautomator.apk", shell=True)


def ensure_env() -> bool:
    p1 = subprocess.run('adb', shell=True, stderr=subprocess.PIPE)
    if p1.stderr is not None:
        print(p1.stderr.reallines())
        print("Please install adb first!")
        return False


if __name__ == '__main__':
    global sysType
    sysType = platform.system()
    config = configparser.ConfigParser()
    config.read('config.Ini')
    mount_dir = config.get('mount', 'target_dir')
    if not mount_smb(config.get('mount', 'root_psw'), config.get('SmbServer', 'server_Dir'),
                     mount_dir, config.get('SmbServer', 'user_name'),
                     config.get('SmbServer', 'user_psw')):
        print('Fail mount {server_dir} to {target_dir}'.format(server_dir=config.get('SmbServer', 'server_Dir'),
                                                               target_dir=mount_dir))

    filepath = './result/htmlreport.html'
    with open(filepath, 'wb') as ftp:
        suite = unittest.TestSuite(unittest.makeSuite(SmokingTest.TestWeekly))
        # suite.addTest(TestWeekly('test01'))
        # suite = unittest.TestSuite()
        # suite.addTest(TestWeekly('test02'))
        runner = HTMLTestReportCN.HTMLTestRunner(stream=ftp, title='Weekly test Result', tester="MD-VAL")
        runner.run(suite)
        unittest.main()
