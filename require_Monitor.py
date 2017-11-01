#coding=utf-8

import urllib
import httplib
import urllib2
import socket
import sys
import unittest
import thread
#unittest.TestCase
class HttpRequire():

    def test_require_Monitor(self,data,rurl):
        req_data=data
        req_data_urlencode=urllib.quote(req_data)
        req_url=rurl
        req=urllib2.Request(url=req_url,data=req_data_urlencode)
        #print req
        socket.setdefaulttimeout(10)
        expected_code='"RESULT":"OK"'
        res=''
        try:

            res_data=urllib2.urlopen(req)
            res=res_data.read()
            assert expected_code in res
            print"验证通过！"

        except:
           errno, errstr = sys.exc_info()[:2]
           if errno == socket.timeout:
               print "响值应超时-A站联程值机失败B站联程机成功"
           else:
               print "联程值机实际结果与预期结果不符，验证失败!"," 预期结果;",expected_code,"；  实际结果：result",res.split("RESULT")[-1].split("ADATYPE")[0]
