import functools
import os
import subprocess
import sys
import time

__all__=["SmokingTest","screenshot"]


def screenshot(func):
    """
    :return:装饰器用于测试抓取截图
    """
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sys.stdout.write("screenshot:../screenshot/{timestamp}.png".format(timestamp=timestamp))
        func(*args, **kwargs)
    path = os.getcwd() + "/screenshot"
    process = subprocess.Popen("adb shell screencap -p /data/local/tmp/screen.png", shell=True)
    process.wait()
    subprocess.run(
        "adb pull /data/local/tmp/screen.png {path}/{timestamp}.png".format(path=path, timestamp=timestamp),
        shell=True)
    subprocess.run("adb shell 'rm /data/local/tmp/screen.png'", shell=True)
    return wrapper