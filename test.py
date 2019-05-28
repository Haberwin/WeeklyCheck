import os
import subprocess
import pexpect
import sys
import time


def mount_smb(sudo_psw,server_dir, target_dir, username, password) -> bool:
    #if os.path.exists(target_dir):
    #subprocess.run("rm -rf {target_dir}".format(target_dir=target_dir), shell=True)
    p1 = subprocess.Popen(
        r"echo {sudo_psw}|sudo -S mount -t cifs {server_dir} {target_dir} -o username={username},password={password}".format(
            sudo_psw=sudo_psw,server_dir=server_dir, target_dir=target_dir, username=username, password=password), shell=True,
        stderr=subprocess.PIPE, encoding='utf-8')
    if p1.stderr is None:
        return True
    err=p1.stderr.readline()
    return( err.__contains__('password') or err.__contains__('mount error(16): Device or resource busy'))


if __name__ == '__main__':
    print(mount_smb('123456','//192.168.4.3/software', r'~/software', 'liuwenhua', '98502'))
