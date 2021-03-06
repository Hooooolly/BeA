from behave import *
from manager import main
import os
import socket
import sys
import subprocess

WD = os.popen("echo $BeA_ROOT").read().strip('\n')

sys.path.append(WD+'/lists')
os.system("python $BeA_ROOT/lists/runlists.py")
from runlists import *


@given('There is incoming traffic')
def step_impl(context):
#Check if there is an incoming packet if there is pass
    hostIP = socket.gethostbyname(socket.gethostname())
    message = 'nmap -p 80 ' + hostIP
    recorded = os.popen(message).read()
    strOpen = "80/tcp open"
    Value = recorded.find(strOpen)
    if (Value != -1):
        pass

@when('All traffic is coming from trusted sources')
def step_impl(context):

    incomingIP = os.popen("sudo netstat -antp | grep 80 | cut -d: -f8 | sort -u").read()
    if incomingIP not in BlackList:
        pass

@then('Allow all traffic')
def step_impl(context):
    main()
    pass

