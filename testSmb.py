import time

from smb.SMBConnection import SMBConnection
import socket

ser_ip='192.168.4.3'
ser_port=139
# 新建连接对象
conn = SMBConnection('liuwenhua', '98502', '', '',use_ntlm_v2=True)
tcp_socket=socket.socket(socket.AF_INET)
# 返回值为布尔型，表示连接成功与否
result = conn.connect(ser_ip, ser_port)
assert conn.auth_result
iTimeNow=time.time()
fStartTime=0.00
for f in conn.listPath('software','VQ405\Weekly'):
    fStartTime=f.create_time if f.create_time>fStartTime  else fStartTime

if(iTimeNow-fStartTime<=7*24*3600):
    print(fStartTime)


# 检索文件
# for f in conn.listPath('share_folder_name','folder_name_in_prvious_one'):
    # print(f.filename)