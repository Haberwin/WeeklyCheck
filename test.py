import sys
import time


class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            sys.stdout.write("screenshot:../screenshot/{timestamp}.png".format(timestamp=timestamp))
            print("[{level}]: enter function {func}()".format( level=self.level,
                func=func.__name__))
            func(*args, **kwargs)
            print("sddddddd")
        return wrapper  # 返回函数

@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

if __name__ == '__main__':
    say("sdad")
    time.sleep(1)
    say("123123")
