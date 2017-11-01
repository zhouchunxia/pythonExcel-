# -*- coding: UTF-8 -*-
import threading
import time
from  require_Monitor import HttpRequire

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread

    def __init__(self,data,url):
        threading.Thread.__init__(self)
        self.req_data = data
        self.req_url = url

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "请求开始 ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        HttpRequire() .test_require_Monitor(self.req_data, self.req_url)
        print "请求结束 " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))



#准备测试数据
data1="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":153419445,\"BFID\":2011016416,\"BINF\":0,\"CNA\":\"肖葵\",\"PRL\":\"QZLWPY\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"XIAOKUI\",\"API02\":\"\",\"API03\":\"MR\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"45272920030813002X\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data2="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":154065509,\"BFID\":2011016414,\"BINF\":0,\"CNA\":\"蓝任欢\",\"PRL\":\"RAIHMC\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"LANRENHUAN\",\"API02\":\"\",\"API03\":\"MR\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"452225198401184534\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data3="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":153011524,\"BFID\":2011016415,\"BINF\":0,\"CNA\":\"苏金平\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"SUJINPING\",\"API02\":\"\",\"API03\":\"MR\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130122196512290727\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"\",\"BAGN\":\"636361/656565/\",\"BAGW\":\"10\",\"BAGA\":\"2\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data4="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":153567368,\"BFID\":2011016410,\"BINF\":0,\"CNA\":\"杨伟\",\"PRL\":\"QZQXHE\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"YANGWEI\",\"API02\":\"\",\"API03\":\"MR\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130634197202232721\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"636363/646464/\",\"BAGW\":\"20\",\"BAGA\":\"2\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data5="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":153011531,\"BFID\":2011016409,\"BINF\":0,\"CNA\":\"杨承霖\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"YANGCHENGLIN\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data6="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":111111111,\"BFID\":144623594,\"BINF\":0,\"CNA\":\"唐兰\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"TAOYIJUN\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data7="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":222222222,\"BFID\":152863484,\"BINF\":0,\"CNA\":\"刘君\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data8="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":333333333,\"BFID\":152915766,\"BINF\":0,\"CNA\":\"黄一力\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data9="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":444444444,\"BFID\":153865908,\"BINF\":0,\"CNA\":\"徐可\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data10="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":555555555,\"BFID\":154028289,\"BINF\":0,\"CNA\":\"刘莉\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data11="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":666666666,\"BFID\":154070722,\"BINF\":0,\"CNA\":\"王琼\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"\",\"BAGN\":\"\",\"BAGW\":\"0\",\"BAGA\":\"0\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data12="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777777,\"BFID\":153155547,\"BINF\":0,\"CNA\":\"董骏\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data13="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777771,\"BFID\":151241105,\"BINF\":0,\"CNA\":\"陈莉\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data14="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777772,\"BFID\":153625901,\"BINF\":0,\"CNA\":\"陈敏\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data15="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777773,\"BFID\":154070721,\"BINF\":0,\"CNA\":\"李磊\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data16="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777774,\"BFID\":153865907,\"BINF\":0,\"CNA\":\"李龙会\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data17="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777775,\"BFID\":152937423,\"BINF\":0,\"CNA\":\"沈东\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data18="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777776,\"BFID\":154054323,\"BINF\":0,\"CNA\":\"郑全\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data19="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777778,\"BFID\":150543210,\"BINF\":0,\"CNA\":\"李志敏\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"
data20="{\"TYPE\":\"1\",\"AFN\":\"9C8643\",\"AFD\":\"16AUG\",\"AFDY\":\"2017-08-16\",\"AOA\":\"SJW\",\"ADA\":\"PVG\",\"OFFN\":\"ADMIN\",\"IP\":\"K15\",\"DATE\":\"2017-08-19 15:35:03.417\",\"passenger\":[{\"BFN\":\"9C8779\",\"BFD\":\"16AUG\",\"BFDY\":\"2017-08-16\",\"BOA\":\"PVG\",\"BDA\":\"SYX\",\"AFID\":777777779,\"BFID\":152915765,\"BINF\":0,\"CNA\":\"刘志文\",\"PRL\":\"QYXVKI\",\"PCN\":\"20161025\",\"PCT\":\"无\",\"API01\":\"HUANGWENYING\",\"API02\":\"\",\"API03\":\"CHD\",\"API04\":\"M\",\"API05\":\"030813\",\"API06\":\"\",\"API07\":\"\",\"API08\":\"I\",\"API09\":\"130185201306090539\",\"API10\":\"\",\"API11\":\"\",\"API12\":\"\",\"API13\":\"\",\"ACC\":\"ADMIN2566666339\",\"PSSR\":\"\",\"BSN\":\"5C\",\"BAGEDA\":\"SYX\",\"BAGN\":\"0089145014\",\"BAGW\":\"1\",\"BAGA\":\"1\",\"BAGFLAG\":\"0\",\"BAGFEE\":\"\",\"ADATYPE\":\"0\"}]}"



#url="http://10.131.10.76:3001/ptm/transfer"
url="http://10.131.0.164:3333/ptm/transfer"


# 创建新线程

thread1 = myThread(data3, url)
thread2 = myThread(data7, url)
thread3 = myThread(data6, url)
thread4 = myThread(data4, url)
thread5 = myThread(data5, url)
thread6 = myThread(data1,url)
thread7 = myThread(data2, url)
thread8 = myThread(data8, url)
thread9 = myThread(data9, url)
thread10 = myThread(data10, url)
thread11 = myThread(data11, url)
thread12 = myThread(data12, url)
thread13 = myThread(data13, url)
thread14 = myThread(data14, url)
thread15 = myThread(data15, url)
thread16 = myThread(data16, url)
thread17 = myThread(data17, url)
thread18 = myThread(data18, url)
thread19 = myThread(data19, url)
thread20 = myThread(data20, url)



# 开启线程

thread6.start()
thread7.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()



