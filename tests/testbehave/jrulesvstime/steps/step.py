#In this step file, there are 10 junk steps before each desired step.
from behave import *
from manager import main
import os
import socket
import sys
import subprocess
WD =os.popen('echo $BeA_ROOT').read().strip('\n')

sys.path.append(WD+'/lists')
os.system('python $BeA_ROOT/lists/runlists.py')
from runlists import *
@given('There1 is1 incoming1 traffic1')
def step_impl(context):
	print 'aaa'
	pass

@given('There2 is2 incoming2 traffic2')
def step_impl(context):
	print 'aaa'
	pass

@given('There3 is3 incoming3 traffic3')
def step_impl(context):
	print 'aaa'
	pass

@given('There4 is4 incoming4 traffic4')
def step_impl(context):
	print 'aaa'
	pass

@given('There5 is5 incoming5 traffic5')
def step_impl(context):
	print 'aaa'
	pass

@given('There6 is6 incoming6 traffic6')
def step_impl(context):
	print 'aaa'
	pass

@given('There7 is7 incoming7 traffic7')
def step_impl(context):
	print 'aaa'
	pass

@given('There8 is8 incoming8 traffic8')
def step_impl(context):
	print 'aaa'
	pass

@given('There9 is9 incoming9 traffic9')
def step_impl(context):
	print 'aaa'
	pass

@given('There10 is10 incoming10 traffic10')
def step_impl(context):
	print 'aaa'
	pass


@given('There is incoming traffic')
def step_impl(context):
	hostIP = socket.gethostbyname(socket.gethostname())
	message = 'nmap -p 80 ' + hostIP
	recorded = os.popen(message).read()
	strOpen = '80/tcp open'
	Value = recorded.find(strOpen)
	if (Value != -1): #if port 80 is open/reciving traffic
		pass
@when('A1 dangerous1 IP1 is1 detected1')
def step_impl(context):
	print 'aaa'
	pass

@when('A2 dangerous2 IP2 is2 detected2')
def step_impl(context):
	print 'aaa'
	pass

@when('A3 dangerous3 IP3 is3 detected3')
def step_impl(context):
	print 'aaa'
	pass

@when('A4 dangerous4 IP4 is4 detected4')
def step_impl(context):
	print 'aaa'
	pass

@when('A5 dangerous5 IP5 is5 detected5')
def step_impl(context):
	print 'aaa'
	pass

@when('A6 dangerous6 IP6 is6 detected6')
def step_impl(context):
	print 'aaa'
	pass

@when('A7 dangerous7 IP7 is7 detected7')
def step_impl(context):
	print 'aaa'
	pass

@when('A8 dangerous8 IP8 is8 detected8')
def step_impl(context):
	print 'aaa'
	pass

@when('A9 dangerous9 IP9 is9 detected9')
def step_impl(context):
	print 'aaa'
	pass

@when('A10 dangerous10 IP10 is10 detected10')
def step_impl(context):
	print 'aaa'
	pass


@when('A dangerous IP is detected')
def step_impl(context):
	incomingIP = os.popen('sudo netstat -antp | grep 80 | cut -d: -f8 | sort -u').read()
	if incomingIP in BlackList:
		pass
@then('Block1 traffic1')
def step_impl(context):
	print 'aaa'
	pass

@then('Block2 traffic2')
def step_impl(context):
	print 'aaa'
	pass

@then('Block3 traffic3')
def step_impl(context):
	print 'aaa'
	pass

@then('Block4 traffic4')
def step_impl(context):
	print 'aaa'
	pass

@then('Block5 traffic5')
def step_impl(context):
	print 'aaa'
	pass

@then('Block6 traffic6')
def step_impl(context):
	print 'aaa'
	pass

@then('Block7 traffic7')
def step_impl(context):
	print 'aaa'
	pass

@then('Block8 traffic8')
def step_impl(context):
	print 'aaa'
	pass

@then('Block9 traffic9')
def step_impl(context):
	print 'aaa'
	pass

@then('Block10 traffic10')
def step_impl(context):
	print 'aaa'
	pass


@then('Block traffic')
def step_impl(context):
	main()
	pass