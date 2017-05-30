import threading
from WindPy import *
w.start();

#define the callback function
def myCallback(indata):
    if indata.ErrorCode!=0:
        print('error code:'+str(indata.ErrorCode)+'\n');
        return();

    global begintime
    lastvalue ="";
    for k in range(0,len(indata.Fields)):
         if(indata.Fields[k] == "RT_LAST"):
            lastvalue = str(indata.Data[k][0]);

    string =  lastvalue +"\n";
    print(string);

    #应该在w.cancelRequest后调用pf.close()
    #pf.close();



exit=False

class feeder(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        w.start()
        w.wsq("IF1512.CFE","rt_time,rt_last",func=myCallback)
#to subscribe if14.CFE

thread1 =feeder(1,"feder-1")
thread1.start()
while(1):
    if (exit):
        break;