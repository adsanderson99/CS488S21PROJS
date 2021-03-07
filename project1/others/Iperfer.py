import socket
import sys
import time

class PortNumberOutOfRange(Exception):
    pass

try: 
    ServerName = sys.argv[1]
    ServerPort = sys.argv[2]
    RunTime = sys.argv[3]
    ServerAddress = (ServerName, ServerPort)
except IndexError as ex1:
    print("Error: missing or additional arguments")

def port_range(ServerPort):
    if ServerPort < 1024 or ServerPort < 65535 :
        msg = 'Error: port number must be in the range 1024 to 65535'
        raise NegativeNumbersNotSupported(msg)

TotalBytes = 0

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket

clientSocket.connect(ServerAddress)

t_end = time.time() + RunTime
while time.time() < t_end:
    
    message = bytes(1000)
    clientSocket.send(message)

    modified_sent = clientSocket.recvfrom(2048)

    TotalBytes = TotalBytes + 1000
    
    continue

clientSocket.close()

print ("Total KB Sent: ", (TotalBytes / 1000), " KB")
print ("Rate: ", ((TotalBytes / 1000000)/RunTime))