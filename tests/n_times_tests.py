import os
import subprocess
from datetime import datetime

TD = os.getcwd()
TDB = TD + '/testbehave'

def tests(test):
    ##Excute a feature and add to excution.log under log folders
    print 'tests function'
    process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write('pkill behave\n')
    commend = 'cd '+ TDB +'/'+test+' && behave\n'
    process.stdin.write(commend)
    result=''
    file=open(TD+'/testlog/testexecution.log','a')
    file.write(str(datetime.now())+'\n')
    for i in range(6):
        temp = process.stdout.readline()
        result=result+temp
        #print result
        file.write(temp)
    file.write('-'*80 + '\n')
    file.close()
    process.terminate()


nTimesInput  = raw_input("n times: ")

nTimes = nTimesInput.split()


log = open('testlog/n_times_tests.csv','a')
log.write('test time: '+str(datetime.now())+'\n')

for i in range(len(nTimes)):

    log.write('One rule repeated for '+nTimes[i] +'times: ,')
    times = int(nTimes[i])
    for j in range(times):
        start = datetime.now()
        tests('n_times_tests')
        end =datetime.now()
        diff = end-start
        print diff

        log.write(str(diff)+',')
log.write('\n')
log.close()


'''

file.write(str(datetime.now())+'\n')

start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f')

    diff = ends - start
    print diff
'''



