import csv
import subprocess

WD = ''

process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process.stdin.write('echo $BDNM_ROOT\n')
WD = process.stdout.readline().strip('\n')
process.terminate()

BlackList = []
with open(WD+'/lists/blacklist.csv', 'rb') as csvfile:
	readerB = csv.reader(csvfile, delimiter='\n')
	for row in readerB:
		temp = row[0].strip(',').split('|')
		if temp[0] == 'A' and (temp[1] not in BlackList):
			BlackList.append(temp[1])

		elif temp[0] == 'R' and temp[1] in BlackList:
			BlackList.remove(temp[1])

		else:
			pass

WhiteList = []

with open(WD+'/lists/whitelist.csv', 'rb') as csvfile:
	readerW = csv.reader(csvfile, delimiter='\n')
	for row in readerW:
		temp = row[0].strip(',').split('|')
		if temp[0] == 'A' and (temp[1] not in WhiteList):
			BlackList.append(temp[1])

		elif temp[0] == 'R' and temp[1] in WhiteList:
			BlackList.remove(temp[1])

		else:
			pass
