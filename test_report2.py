#coding:utf-8
import MySQLdb
import pymssql
import datetime
import sys
import codecs

class MSSQL(object):
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db =db

    def _GetConnect(self):
        if not self.db:
            raise(NameError,'Wrong settings for database')
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,'Failed to connect')
        else:
            #此处来连接中文数据库
            cur.execute(u'use '+self.db)
        return cur

    def ExecQuery(self,sql):
        cur = self._GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self._GetConnect()
        cur.execute(sql)
        self.conn.commit() 
        self.conn.close()

#定义全局变量
alist = []

def main():
    strCQDB = ["aviation_hcc_db0","aviation_vms_db","aviation_foc_db","aviation_dcs_db","aviation_fcs_db","aviation_fcs_core_db",
    "aviation_smp_db0","aviation_flytrain_db","aviation_wechat_db","aviation_shop_db",
    "aviation_contract_db","aviation_orm_db","aviation_bpms_db","aviation_spms_db",u'aviation_移动招聘_db',u'aviation_机上销售平台_db',u'external_智慧景区_db']
    strSHDB = ["aviation_td_smis_db","aviation_td_mis1_db","research_td_spring3g_db","website_td_springairlines_db"]
    
    sdb = "aviation_dcs_db"
    scycle = u'台湾预检报文(V4)'
    s_time = "1"  #默认的修改用例实际耗时
    s_etime = "1"  #默认的测试实际执行耗时
    
    if sdb in strCQDB:
        host = "10.131.0.15"
        user = "reader"
        pwd = "CZYZLBqa"
    else:
        if sdb in strSHDB:
            host = "192.168.0.216"
            user = "testcq"
            pwd = "test1234"
        else:
            host = "10.32.0.110"
            user = "chongqing"
            pwd = "chongqing"

    now = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    file_BUG = 'test_repot_'+now+'.txt'
    print "BEGIN:"+sdb+","+scycle+","+host+","+user+","+pwd
    tid = get_tcid(host,pwd,user,sdb,scycle) #获取当前节点id
    nlist = get_fid(host,pwd,user,sdb,tid) #获取该id下的所有子节点id
    FindLastChildNode(host,pwd,user,sdb,tid,nlist)#获取到这个测试用例集的全部最底层路径文件夹存入alist
    print "----over find leaf----"
    for ss in alist:
        print "lll:"+str(ss)
    all_report = "" #定义总输出结果字符串
    for i in alist:
        all_report = all_report+one_test_set(host,pwd,user,sdb,i,s_time,s_etime)
    write_To_txt_bug(file_BUG,all_report.encode('latin1').decode('gbk'))

#IO写入中文文件txt
def write_To_txt_bug(file_name,data):
    file_object = codecs.open(file_name,'a',encoding = 'utf-8')
    file_object.write(codecs.BOM_UTF8)
    file_object.write(data+'\r\n')
    file_object.close( )

#获取执行记录对应的BUG
def read_bug(host,pwd,user,db,rid):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ms = MSSQL(host,user,pwd,db)
    #获取BUG数
    sql1 = "SELECT L.LN_BUG_ID,B.BG_SEVERITY FROM "+db+".td.LINK L,"+db+".td.BUG B WHERE L.LN_ENTITY_TYPE = 'STEP' AND L.LN_ENTITY_ID IN (SELECT T.ST_ID FROM "+db+".td.STEP T WHERE T.ST_RUN_ID="+rid+" AND T.ST_STATUS = 'failed') AND L.LN_BUG_ID=B.BG_BUG_ID"
    #print sql1
    test_list = ms.ExecQuery(sql1.encode('utf8'))
    return test_list

#QC统计数据（中文）——统计所有测试用例和执行记录
def read_test(host,pwd,user,db,sid):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ms = MSSQL(host,user,pwd,db)
    #获取BUG数
    sql1 = "SELECT e.n5,e.n3,e.n1,e.n2,e.n4,f.RN_RUN_NAME,f.RN_EXECUTION_DATE,f.RN_TESTER_NAME,f.RN_RUN_ID FROM (SELECT t.TS_NAME  AS n1,t.TS_STEPS AS n2,c.CYID AS n3,c.CY AS n4,T.TS_TEST_ID AS n5 FROM "+db+".td.TEST T, "+db+".td.TESTCYCL d,(SELECT b.CY_CYCLE_ID AS CYID,b.CY_CYCLE AS CY FROM "+db+".td.CYCL_FOLD a,"+db+".td.CYCLE b WHERE a.CF_ITEM_ID = "+str(sid)+" AND a.CF_ITEM_ID = b.CY_FOLDER_ID ) C WHERE d.TC_TEST_ID=t.TS_TEST_ID AND C.CYID = d.TC_CYCLE_ID) e,"+db+".td.RUN f WHERE e.n3=f.RN_CYCLE_ID and e.n5 = f.RN_TEST_ID"
    #print sql1
    test_list = ms.ExecQuery(sql1.encode('utf8'))
    return test_list

#获取测试用例文件夹id
def get_tcid(host,pwd,user,db,scycle):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ms = MSSQL(host,user,pwd,db)
    #获取BUG数
    sql1 = "select a.CF_ITEM_ID from "+db+".td.CYCL_FOLD a where a.CF_ITEM_NAME = '"+scycle+"'"
    #print sql1
    test_list = ms.ExecQuery(sql1.encode('utf8'))
    id = 0
    for a in test_list:
        id = a[0]
    return id

#根据父id获取id
def get_fid(host,pwd,user,db,cid):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ms = MSSQL(host,user,pwd,db)
    sql1 = "select a.CF_ITEM_ID from "+db+".td.CYCL_FOLD a where a.CF_FATHER_ID = "+str(cid)
    #print sql1
    test_list = ms.ExecQuery(sql1.encode('utf8'))
    return test_list

#遍历找到所有最底层的测试用例集文件夹
def FindLastChildNode(host,pwd,user,db,node,list):
    if list:
        for i in list:
            d = get_fid(host,pwd,user,db,i[0])
            FindLastChildNode(host,pwd,user,db,i[0],d)
    else:
        alist.append(node)
        return

#单个用例集数据生成,返回用例集的
def one_test_set(host,pwd,user,sdb,sid,s_time,s_etime):
    test_list = read_test(host,pwd,user,sdb,sid)
    #组装信息存放到dic_test[用例集id]：测试人员、需求名称、用例步骤数、测试用例、测试日期、测试日志、BUG数
    dic_run = {} #存放Run的信息
    dic_test = {} #存放总信息
    dic_bug = {} #存放BUG信息
    dic_step = {} #存放用例步骤数
    report_list = []
    for t in test_list:
        tid,id,test,step,req,run,exet,tester,rid = t
        dic_step[tid] = step
        #获取Run的BUG信息
        bug_list = read_bug(host,pwd,user,sdb,str(rid))
        for b in bug_list:
            bid,bss = b
            if tid in dic_bug.keys():
                dic_bug[tid] = dic_bug[tid]+";"+str(bid)+"/"+str(bss)+"/1"
            else:
                dic_bug[tid] = str(bid)+"/"+str(bss)+"/1"
        #获取用例信息
        if tid not in dic_run.keys():
            dic_run[tid] = run
        else:
            dic_run[tid]=dic_run[tid] + ";" +run
        if tid not in dic_test.keys():
            dic_test[tid] = str(tester)+","+req+","+str(step)+","+req+","+test+","+str(exet)+","+str(step)+","+s_time
    data = ""
    for key in dic_test:
        #dic_test[key] = dic_test[key] +","+ dic_run[key]+","+dic_bug[id]
        bug_num = 0 #Bug数默认是0
        hnum = 0 #回归次数默认是0
        if key in dic_run:
            runn = dic_run[key]
            hnum = runn.count(';') #回归次数等于run的分号数
        sbug = "" #BUG详情，默认是空，没有BUG
        if key in dic_bug:
            sbug = dic_bug[key]
            bug_num = sbug.count(';')+1
        enum = (hnum+1)*dic_step[key] #回归次数+1乘以用例步骤书等于执行步骤数
        bl = float(bug_num)/enum #BUG数/执行用例步骤数等于BUG率
        data = data+dic_test[key] +","+ dic_run[key]+","+s_etime+","+str(enum)+","+sbug+","+str(hnum)+","+str(bl)+'\r\n'
    print "one:"+str(sid)
    return data

if __name__ == '__main__':
    global alist
    main()






