#_*_coding:utf-8_*_

# 20181201 11:09 SUNDAY

import socket
import sys

host = "www.baidu.com"
#host = "www.cnblogs.com"
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname could not be resolved. Exiting"
    sys.exit()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((remote_ip,port))


msg = "GET / HTTP/1.1\r\n\r\n"

# 发送数据
try:
    s.sendall(msg)
except socket.error:
    print "Send failed"
    sys.exit()

#接收数据
reply = s.recv(4096)

print reply

# 关闭Socket
s.close()
