#################################################
###  Behave-Driven Network Management Server  ###
### Jiayi Wang, Thomas Merod, Flavio Esposito ###
### St Louis University, Computer Science Dep.###
###        Last Edit: Oct 9, 2017             ###
#################################################

import socket
import sys
import subprocess
import os
from datetime import datetime


###Server##
#GLOBAL VARs#


version = '1.0'
IP = 'localhost'
port = 10002

Controller = 'Ryu'

#CITATIONs#
spliter = ','
spliterF = '/' #spliter for feature content


#HEADERS#
Action = 'ACT'
Handshake = 'HSK'
Quit = 'QUT'
Reply = 'RPL'

#Actions#
Create = 'create feature'
Alter = 'alter feature'
Excute = 'excute'
SyncList = 'sync list'


#Reply Stutas#
replyRetry = 'RETRY'
replySuccess = 'SUCCESS'
replyFail = 'FAIL'


#Content Type#
ServiceName = 'serviceName'
FeatureContent = 'featureContent'
Blacklist = 'blacklist'
Whitelist = 'whitelist'

#Root Path#
WD = '' #Working directory
WDB = '' #Working directory/beheave


#####HELPER FUNCTIONS####

def sp(list,spliter):
    #put list of items into a string with spliters
    temp=''
    for i in list:
        temp = temp+i + spliter
    return temp[:-len(spliter)]

def pwd():
    #Feeding the working directory global variable, return 1 if success.
    global WD, WDB
    process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write('echo $BDNM_ROOT\n')
    WD = process.stdout.readline().strip('\n')
    WDB = WD + '/behave'
    process.terminate()
    #print WD
    #print WDB

    if WD == '':
        return 0
    else:
        return 1


####FUNCTIONS####

def ServiceExistCheck(Servicename):
    #Check if the folder with the servicename exist under beheave folder, return True if exist
    print 'namecheck function'
    folder = WDB+'/'+ Servicename
    #print 'folder: '+ folder
    process = subprocess.Popen(['/bin/bash'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    commend = "test -d " +folder+ " && echo 1 || echo 0\n"
    #print commend
    process.stdin.write(commend)
    out = process.stdout.readline().strip('\n')
    #print out
    process.terminate()
    if out == '1':
        return True
    else:
        return False


def Excution(service):
    ##Excute a feature and add to excution.log under log folders
    print 'Excution function'
    process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    commend = 'cd '+ WDB +'/'+service+' && behave\n'
    process.stdin.write(commend)
    result=''
    file=open(WD+'/log/excution.log','a')
    file.write(str(datetime.now())+'\n')
    for i in range(6):
        temp = process.stdout.readline()
        result=result+temp
        print result
        file.write(temp)
    file.write('-'*80 + '\n')
    file.close()
    process.terminate()
    return result

def writeFeature(content):
    #write into feature file in format
    print 'Write Feature Function'
    try:    
        items = content.split(spliterF)
        name = items[0] + '.feature'
        path = WDB+'/'+items[0]+'/'+name
        file = open(path, 'w')  
        file.write('Feature: '+items[1]+'\n')
        file.write('    Scenario: '+items[2]+'\n')
        file.write('        Given '+items[3]+'\n')
        file.write('        When '+items[4]+'\n')
        file.write('        Then '+items[5]+'\n')
        file.close()
        return True
    except:
        return False
    

def mkdir(name):
    #create new directory folder under behave/
    print 'mkdir Function'
    subdirectory = 'behave/'+name
    try:
        os.mkdir(subdirectory)
        return True
    except Exception:
        pass
    return False


def listOp(listName, content):
    #add item to list
    try:
        file = open(WD+'/lists/'+listName+'.csv', 'a')
        file.write(content + ',\n')
        file.close()
        return True
    except:
        return False
    
def action(action, contentType, content):
    print "Action Function"
    if action==Excute and contentType == ServiceName:
        print 'here'
        if ServiceExistCheck(content)==True:

            result = Excution(content)
            
            return sp([Reply ,action ,ServiceName,replySuccess,result],spliter)
        else:
            return sp([Reply,action,ServiceName ,replyRetry,'No Such Servcie'],spliter)
    elif action == Create and contentType == ServiceName:
        if ServiceExistCheck(content)==False:
            return sp([Reply, action ,ServiceName,replySuccess,content,'Waiting for Feature Input:'],spliter)
        else:
            return sp([Reply,action ,ServiceName ,replyRetry ,content," can't be create. Feature file already exist."],spliter)
        
    elif action == Alter and contentType == ServiceName:
        if ServiceExistCheck(content)==True:
            return sp([Reply,action,ServiceName,replySuccess,content ,'Waiting for Feature Input.'],spliter)
        else:
            return sp([Reply,action,ServiceName,replyRetry,content,"can't alter. Feature file is not exist."],spliter)
        
    elif action == Create and contentType == FeatureContent:
        items = content.split(spliterF)
        name = items[0]
        if mkdir(name)== False:
            return sp([Reply,action,FeatureContent,replyRetry,name,"Error creating new folder"], spliter)
        if ServiceExistCheck(name) == True and writeFeature(content)== True:
            return sp([Reply,action,FeatureContent,replySuccess,name,"Featuer File Created"],spliter)
        else:
            return sp([Reply,action,FeatureContent,replyRetry,name,"Error"],spliter)
    elif action == Alter and contentType == FeatureContent:
        if writeFeature(content)== True:
            items = content.split(spliterF)
            name = items[0]
            return sp([Reply,action , FeatureContent,replySuccess, name , "Feature File Changed"],spliter)
        else:
            return sp([Reply,action,FeatureContent,replyRetry ,name ,"Error"],spliter)
    elif action == SyncList:
        if listOp(contentType, content)==True:
            return sp([Reply,action,contentType,replySuccess,contentType+" Updated"],spliter)
        else:
            return sp([Reply ,action,contentType ,replyRetry,contentType+" Update Error"],spliter)
    return "Fail"





###OPEN CONNECTION###
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, port)
sock.bind(server_address)

sock.listen(1)

if pwd() == 0:
    print 'error getting directory'
    connection.sendall(replyFail)
    exit()

while True:
    
    ###LISTENING##
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Connection Set Up
        HasBeenHandshake = False
        while True:
            print 'waiting for a command'
            message = connection.recv(1000)
            print 'recving ' + message
            if message:
                buff = message.split(spliter)
                if HasBeenHandshake == False:
                    print "HandShak phasse"
                    if buff[0] == version and buff[1]==Controller:
                        connection.sendall(sp([Handshake,replySuccess],spliter))
                        HasBeenHandshake = True
                        print >>sys.stderr, 'Handshake Success'
                        continue
                    else:
                        connection.sendall(sp[Handshake,replyFail],spliter)
                        continue

                #Actions#
                else:
                    if buff[0] == Quit:
                        print "Client Quiting"
                        connection.close()
                        break

                    elif buff[0] == Action:
                        print "receiving action message correctly: "+ message
                        result = action(buff[1], buff[2], buff[3])
                        
                        connection.sendall(result)
                        continue              
                            

                    else:
                        connection.sendall(replyFail)
                        print 'Sending Fail'
                        break
                    
    finally:
        # Clean up the connection
        connection.close()


