#jrules*ntimesvstime


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

def generateJunkRules(n):
    i = 1
    file=open('testbehave/jrulesvstime/steps/step.py','w')
    file.write("#In this step file, there are "+str(n)+" junk steps before each desired step.\n")
    file.write("from behave import *\nfrom manager import main\nimport os\nimport socket\nimport sys\nimport subprocess\nWD =os.popen('echo $BeA_ROOT').read().strip('\\n')\n\nsys.path.append(WD+'/lists')\nos.system('python $BeA_ROOT/lists/runlists.py')\nfrom runlists import *")

    while i <= n:
        file.write("\n@given('There"+str(i)+" is"+str(i)+" incoming"+str(i)+" traffic"+str(i)+"')\ndef step_impl(context):\n\tprint 'aaa'\n\tpass\n")
        i+=1
        #file.write(given)
    file.write("\n\n@given('There is incoming traffic')\ndef step_impl(context):\n\thostIP = socket.gethostbyname(socket.gethostname())\n\tmessage = 'nmap -p 80 ' + hostIP\n\trecorded = os.popen(message).read()\n\tstrOpen = '80/tcp open'\n\tValue = recorded.find(strOpen)\n\tif (Value != -1): #if port 80 is open/reciving traffic\n\t\tpass")
    i=1

    while i <= n:
        when="\n@when('A"+str(i)+" dangerous"+str(i)+" IP"+str(i)+" is"+str(i)+" detected"+str(i)+"')\ndef step_impl(context):\n\tprint 'aaa'\n\tpass\n"
        file.write(when)
        i+=1

    file.write("\n\n@when('A dangerous IP is detected')\ndef step_impl(context):\n\tincomingIP = os.popen('sudo netstat -antp | grep 80 | cut -d: -f8 | sort -u').read()\n\tif incomingIP in BlackList:\n\t\tpass")
    i=1
    while i <= n:
        then="\n@then('Block"+str(i)+" traffic"+str(i)+"')\ndef step_impl(context):\n\tprint 'aaa'\n\tpass\n"

        file.write(then)
        i+=1

    file.write("\n\n@then('Block traffic')\ndef step_impl(context):\n\tmain()\n\tpass")
    file.close()

jrulesInput  = raw_input("junk rules: ")

jrules = jrulesInput.split()

nTimesInput  = raw_input("n times: ")

nTimes = int(nTimesInput)


log = open('testlog/jrules*ntimesvstime.csv','a')
log.write('test time: '+str(datetime.now())+'\n')
log.write('jrules\\n times')
for a in range(nTimes):
    log.write(','+str(a+1))

log.write('\n')

for i in range(len(jrules)):
    log.write(jrules[i])
    rules = int(jrules[i])
    generateJunkRules(rules)
    for j in range(nTimes):
        start = datetime.now()
        tests('jrules*ntimesvstime')
        end =datetime.now()
        diff = end-start

        log.write(','+str(diff))
    log.write('\n')
log.close()


'''

file.write(str(datetime.now())+'\n')

start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f')

    diff = ends - start
    print diff
'''



