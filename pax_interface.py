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

def sigIntHander(signo,frame):
    print 'get signo# ',signo
    global runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)

strHost = "10.131.11.94"
HOST = strHost #socket.inet_pton(socket.AF_INET,strHost)
PORT = 3113

httpheader = '''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''

lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lisfd.bind((HOST, PORT))
lisfd.listen(2)

signal.signal(signal.SIGINT,sigIntHander)

global confd
runflag = True
while runflag:
    try:
        confd,addr = lisfd.accept()
        print "接收到请求数据时间 ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    except socket.error as e:
        if e.errno == errno.EINTR:
            print 'get a except EINTR'
        else:
            raise
        continue

    if runflag == False:
        break;

    print "connect by ",addr
    data = confd.recv(8192)
    if not data:
        break
    rev_data=data.split("pushInfo")[-1]
    aa=urllib.unquote(rev_data)
    print '打印接收到的数据',aa
    time.sleep(2)
    confd.send(HttpResponse(httpheader))
    print "返回数据时间： ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print "返回数据为：",HttpResponse(httpheader)
    confd.close()
else:
    print 'runflag#',runflag

print 'Done'