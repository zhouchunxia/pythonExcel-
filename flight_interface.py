# -*- coding: UTF-8 -*-
import socket
import signal
import errno
import urllib
import time
from time import sleep

def HttpResponse(header):
     #response = "{\"code\":\"success\",\"msg\":\"成功\",\"data\":\"\",\"extend\":\"\"}"
     #return response
    #f = file(wtext)
    #contxtlist = f.readlines()
    context = "{\"code\":\"success\",\"msg\":\"成功\",\"data\":\"\",\"extend\":\"\"}"
    response = "%s %d\n\n%s\n\n" % (header,len(context),context)
    return response

def sigIntHander():
    global runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)

HOST = "10.131.11.94"
PORT = 3223

httpheader = '''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''

lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lisfd.bind((HOST, PORT))
#操作系统可以挂起的最大连接数量
lisfd.listen(5)
#信号处理模块(信号量，信号处理模块)
signal.signal(signal.SIGINT,sigIntHander)

global confd
runflag = True
while runflag:
    try:
        confd,addr = lisfd.accept()
        print "接收到请求时间 ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    except socket.error as e:
        if e.errno == errno.EINTR:
            print 'get a except EINTR'
        else:
            raise
        continue

    if runflag == False:
        break;

    print "connect by ",addr
    data = confd.recv(60480)
    rev_data=urllib.unquote(data)
    if not data:
        break
    rev_data=data.split("pushInfo")[-1]
    print '打印接收到的数据',urllib.unquote(rev_data)

    #time.sleep(14)
    confd.send(HttpResponse(httpheader))
    print "返回数据时间： ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print "返回数据为：",HttpResponse(httpheader)

    confd.close()
else:
    print 'runflag#',runflag

print 'Done'