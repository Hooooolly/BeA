#################################################
###    Behavior-Driven Architecture Client    ###
### Jiayi Wang, Thomas Merod, Flavio Esposito ###
### St Louis University, Computer Science Dep.###
###        Last Edit: April 28, 2018          ###
#################################################

import socket
import sys

##Client##
#GLOBAL VARs#

version = '1.01'
IP = 'localhost'
port = 10000

server_address = (IP, port)
Controller = 'Ryu'


#ACTIONS#
Create = 'create feature'
Alter = 'alter feature'
Execute = 'execute'
SyncList = 'sync list'




#NOTATION#
spliter = ','
spliterF = '/'



#HEADER#
Action = 'ACT'
Handshake = 'HSK'
Quit = 'QUT'
Reply = 'RPL'

#Reply Stutas#
replyRetry = 'RETRY'
replySuccess = 'SUCCESS'
replyFail = 'FAIL'

#Content Type
ServiceName = 'serviceName'
FeatureContent = 'featureContent'
Blacklist = 'blacklist'
Whitelist = 'whitelist'


#####HELPER FUNCTIONS####

def sp(list,spliter):
    #put list of items into a string with spliters  
	temp=''
	for i in list:
	    temp = temp+i + spliter
	return temp[:-len(spliter)]

def handshakeMessage():
    return sp([version,Controller,IP],spliter)

def isHandshake(message):
    if message[0] == Handshake:
        if message[1] ==replySuccess: #Handshake success
            welcome()
            return True
        else:
            print 'Handshake Fail'
            return False
def welcome():
    print '#'*53
    print '###    Welcom to Behavior-Driven Architecture!    ###'
    print '###     -- The only English-base network manager! ###'
    print '#'*53

def printResult(result): 
    #print result from server
    print '=====Server message====='
    print result

def actionMessage():
    ##MESSAGE TYPE, ACTION, CONTENT TYPE, CONTENT##
    inp = ''
    actipn =''
    print '-'*60
    #while action != Create and action != Alter  and action != Execute and action != 'quit' and action!=SyncList:
    while inp != 'c' and inp != 'a'  and inp != 'e' and inp != 'q' and inp !='sl':
        #action = raw_input("What is the action that you want to do?\n( execute / create feature / alter feature / sync list / quit ):\n")
        inp = raw_input("What is the action that you want to do?\n( e (execute) / c (create feature) / a (alter feature) / sl (sync list) / q (quit) ):\n")
        if inp == 'c':
            action = Create
        elif inp == 'a':
            action = Alter
        elif inp == 'e':
            action = Execute
        elif inp == 'q':
            action = Quit
        elif inp == 'sl':
            action = SyncList
    #print action
    if action == Quit:
        return QUT
    elif action == Execute or action ==  Create or  action == Alter:
        return sp([Action,action,ServiceName,raw_input('Service Name you want to execute or change: ')], spliter)
    elif action == SyncList:
        List = ''
        op = ''
        while (List != Blacklist or List!= Whitelist) and ( op!= 'add' and op!='remove'):
            listOpTemp = raw_input("Enter in this format: {blacklist/whitelist} {add/remove} {ip address}: \n")
            listOp =listOpTemp.split()
            if len(listOp)!=3:
                continue
            #print listOp
            List = listOp[0]
            op = listOp[1]
            ip = listOp[2]
        if op == 'add':
            content = 'A' + '|' + ip
        else:
            content = 'R' + '|' + ip
        return sp([Action,action,List,content],spliter) 

def actionRetry(warning):
    print '--Server message--'
    print warning
    return actionMessage()

def featureInput(name): #return a string for feture file input

    feature = raw_input("Feature: ")
    scenario = raw_input("Scenario: ")
    given = raw_input("Given: ")
    when = raw_input("When: ")
    then = raw_input("Then: ")

    return sp([name,feature,scenario,given,when,then],spliterF)


def featureMessage(action,name):
    return sp([Action,action,FeatureContent,featureInput(name)],spliter)



while True:
    ###START###
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(server_address)
    #sp('a','b')

    #Sending handshake message
    HasBeenHandshake = False
    sock.sendall(handshakeMessage())

    try:
        ###LISTENING###
        while True:
            buff = sock.recv(10000)

            if buff:
                message = buff.split(spliter)

                ##Whenever received Fail, quit
                if message[0]== replyFail:
                    break

                
                ###LISTEN FOR HANDSHAKE###
                if HasBeenHandshake == False:
                    if isHandshake(message)==True:
                        HasBeenHandshake = True


                        sock.sendall(actionMessage())
                        continue
                    else:
                        print 'retry handshake'
                        sock.sendall(handshakeMessage())
                        continue
                
                ###LISTEN FOR Action Message Reply###
                ##Action Type, ContentType, Reply Type, Result/Warning
                elif message[0]== Reply:
                    if message[1]== Execute :
                        print 'Received: Execute Reply: '
                        #print buff
                        if message[3]== replyRetry:
                            sock.sendall(actionRetry(message[4]))

                        elif message[3]==replySuccess:
                            printResult(message[4])
                            sock.sendall(actionMessage())
                            continue
                        else:
                            break
                        
                        continue
                    elif message[1] == SyncList:
                        printResult(message[4])
                        sock.sendall(actionMessage())
                        continue
                    elif (message[1]== Create or Alter):
                        if message[2] ==ServiceName:
                            if message[3]== replyRetry:
                                sock.sendall(actionRetry(message[4]+message[5]))
                            elif message[3] == replySuccess:
                            	printResult(message[5])
                                sock.sendall(featureMessage(message[1],message[4]))
                            else:
                                break
                            continue
                        elif message[2] == FeatureContent:
                            if message[3]== replyRetry:
                            	printResult(message[5])
                                sock.sendall(featureMessage(message[1],message[4]))
                                continue
                            elif message[3] == replySuccess:
                            	printResult(message[5])
                                sock.sendall(actionMessage())
                                continue


            else:
                ##TERMINATION##
                print 'nothing recvd'
                break

    finally:
        print >>sys.stderr, 'Client Closing, Bye!'
        sock.sendall(Quit)
        sock.close()
        break
