import os

os.system('iptables -F')
os.system('iptables -P INPUT DROP')
os.system('iptables -P OUTPUT DROP')
os.system('iptables -P FORWARD DROP')

