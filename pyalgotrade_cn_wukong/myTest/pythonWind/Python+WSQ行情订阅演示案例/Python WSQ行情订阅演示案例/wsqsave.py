# coding: UTF-8
# 说明：
# 该案例是演示wsq实时行情订阅的使用，订阅模式主要有两部分组成，一部分是用wsq函数订阅所需要的行情，
# 另一部分是编写自己的回调函数，用于处理实时推送过来的行情数据
# myCallback(indata) 即为本案例所使用的回调函数，回调函数有且只能有一个参数：indata
# indata的数据结构如下：
# indata.ErrorCode 错误码，如果为0表示运行正常
# indata.StateCode 状态字段，使用时无需处理
# indata.RequestID 存放对应wsq请求的RequestID
# indata.Codes 存放行情对应的code
# indata.Fields 存放行情数据对应的指标
# indata.Times 存放本地时间，注意这个不是行情对应的时间，要获取行情对应的时间，请订阅rt_time指标
# indata.Data 存放行情数据

# 取消订阅可使用w.cancelRequest(requestID),如果想取消全部订阅，可使用w.cancelRequest(0)

#例如:
# indata.ErrorCode=0
# indata.StateCode=1
# indata.RequestID=3
# indata.Codes=[IF.CFE]
# indata.Fields=[RT_LAST]
# indata.Times=[20151123 15:12:40]
# indata.Data=[[3623.0]]


from WindPy import *
w.start();

#open a file to write.
pf = open('c:\\pywsqdataif.data', 'w')

#define the callback function
#用于处理行情的回调函数
def myCallback(indata):
    print indata
    if indata.ErrorCode!=0:
        print('error code:'+str(indata.ErrorCode)+'\n');
        return();

    global begintime
    lastvalue ="";
    for k in range(0,len(indata.Fields)):
         if(indata.Fields[k] == "RT_TIME"):
            begintime = indata.Data[k][0];
         if(indata.Fields[k] == "RT_LAST"):
            lastvalue = str(indata.Data[k][0]);

    string = str(begintime) + " " + lastvalue +"\n";
    pf.writelines(string)
    print(string);
    pf.flush();

    #想要结束订阅，可使用w.cancelRequest(0)命令，然后后调用pf.close()关闭文件
    #pf.close();


#订阅行情
w.wsq("IF.CFE","rt_time,rt_last",func=myCallback)
while(1):
    info="这个while循环主要是防止IDE在运行或者debug时，运行w.wsq()语句后就退出，从而导致行情推送过来后，回调函数无法运行！";